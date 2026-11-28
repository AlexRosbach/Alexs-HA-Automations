from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


scanner = load('run_gitleaks')
staged = load('check_staged')


class SecretScanningTests(unittest.TestCase):
    def test_literal_fix_does_not_touch_other_values(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'repo'
            snapshot = Path(folder) / 'snapshot'
            root.mkdir(); snapshot.mkdir()
            value = 'synthetic-' + 'credential-for-unit-test'
            path = root / 'example.yaml'
            path.write_text(f'password: {value}\nmode: single\n')
            count = scanner.replace_findings(root, snapshot, [
                {'File': str(snapshot / 'example.yaml'), 'Secret': value}
            ])
            self.assertEqual(count, 1)
            self.assertEqual(path.read_text(), 'password: REPLACE_WITH_YOUR_OWN_SECRET\nmode: single\n')

    def test_outside_finding_cannot_overwrite_other_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'repo'; root.mkdir()
            snapshot = Path(folder) / 'snapshot'; snapshot.mkdir()
            outside = Path(folder) / 'outside.txt'; outside.write_text('unchanged')
            with self.assertRaises(scanner.ScanError):
                scanner.replace_findings(root, snapshot, [{'File': str(outside), 'Secret': 'unchanged'}])
            self.assertEqual(outside.read_text(), 'unchanged')

    def test_ambiguous_encoded_finding_is_not_replaced(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'repo'; root.mkdir()
            snapshot = Path(folder) / 'snapshot'; snapshot.mkdir()
            (root / 'value.txt').write_text('encoded-value')
            with self.assertRaises(scanner.ScanError):
                scanner.replace_findings(root, snapshot, [{'File': 'value.txt', 'Secret': 'decoded-value'}])
            self.assertEqual((root / 'value.txt').read_text(), 'encoded-value')

    def test_git_index_is_checked_instead_of_cleaned_worktree(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'repo'; root.mkdir()
            snapshot = Path(folder) / 'snapshot'; snapshot.mkdir()
            subprocess.run(['git', 'init', '-q', str(root)], check=True, capture_output=True)
            path = root / 'sample.yaml'
            original = 'password: ' + 'test-' + 'private-value\n'
            path.write_text(original)
            subprocess.run(['git', '-C', str(root), 'add', 'sample.yaml'], check=True, capture_output=True)
            path.write_text('password: REPLACE_WITH_YOUR_OWN_SECRET\n')
            staged.export_index(root, snapshot)
            self.assertEqual((snapshot / 'sample.yaml').read_text(), original)
            self.assertNotEqual((snapshot / 'sample.yaml').read_text(), path.read_text())

    def test_ignore_file_cannot_suppress_scanning(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / '.gitleaksignore').write_text('synthetic-fingerprint\n')
            with self.assertRaises(scanner.ScanError):
                scanner.scan(root, 'tree')

    def test_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'repo'; root.mkdir()
            outside = Path(folder) / 'outside'; outside.write_text('private')
            (root / 'link').symlink_to(outside)
            with self.assertRaises(scanner.ScanError):
                scanner.repository_files(root)


if __name__ == '__main__':
    unittest.main()
