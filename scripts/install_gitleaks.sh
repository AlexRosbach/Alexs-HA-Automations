#!/usr/bin/env bash
# Pinned official Linux x86_64 release; verify before executing anything.
set -euo pipefail
if [[ "$(uname -s)/$(uname -m)" != "Linux/x86_64" ]]; then
  echo 'Install Gitleaks 8.30.1 for your platform and put it on PATH.' >&2
  exit 1
fi
install_dir="${1:-.tools/bin}"
archive_dir="$(mktemp -d)"
trap 'rm -rf "$archive_dir"' EXIT
curl --fail --silent --show-error --location --retry 3 \
  --proto '=https' --tlsv1.2 \
  'https://github.com/gitleaks/gitleaks/releases/download/v8.30.1/gitleaks_8.30.1_linux_x64.tar.gz' \
  --output "$archive_dir/gitleaks.tar.gz"
python3 - "$archive_dir/gitleaks.tar.gz" <<'PY'
import hashlib
import pathlib
import sys
expected = '551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb'
if hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest() != expected:
    raise SystemExit('Gitleaks checksum verification failed.')
PY
tar -xzf "$archive_dir/gitleaks.tar.gz" -C "$archive_dir" gitleaks
mkdir -p "$install_dir"
install -m 0755 "$archive_dir/gitleaks" "$install_dir/gitleaks"
echo 'Installed checksum-verified Gitleaks 8.30.1.'
