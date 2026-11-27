# Agent checklist for publishing automations

1. Keep original exports outside this public repository and work in a temporary staging directory.
2. Sanitize the configuration before writing public output, including custom service names, dictionary keys, recipients, templates and numeric identifiers.
3. Preserve only reviewed generic Home Assistant concepts. Replace private data with consistent neutral placeholders; keep real secrets in the user's local configuration.
4. Generate a descriptive category and behavior name using `scripts/catalogue.py`. Do not use numbered export positions or invent a purpose that is no longer present in the anonymized data.
5. Derive `metadata.json`, the YAML alias and description, and the example README from the same reviewed vocabulary. Keep all examples when names collide; use the generated stable variant fingerprint.
6. State clearly when missing trigger values, expressions or conditions need reconstruction before the example can run.
   Write reader-facing explanations in simple German. Keep stable paths and canonical YAML labels separate from friendly documentation titles, explain required helpers/scripts, and link the beginner guide.
7. Regenerate the root README catalogue and all example READMEs with `python scripts/catalogue.py --write`, then verify them with `--check`.
8. Run the [security and privacy checks](security-and-privacy.md), including the local check before the commit. Review findings without printing private values in logs or public comments.
9. Verify YAML syntax, catalogue links, consistent placeholders and safe output paths. Do not follow symlinks or overwrite unrelated source files.
10. Publish only the reviewed sanitized output. If sensitive material was already committed, handle its Git history separately and rotate exposed credentials; a new cleanup commit is not historical erasure.

An example is publishable only when its public purpose is understandable and its content has passed the repository policy. Automated checks cannot prove that arbitrary free text contains no private information.
