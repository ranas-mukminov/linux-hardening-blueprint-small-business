# Contributing Guidelines

Thanks for your interest in improving the Linux Hardening Blueprint. We welcome community ideas, documentation fixes, bug reports, and new tests. To keep the project predictable and safe for production users, follow these rules:

1. **Discuss first** – Open an issue describing the problem, risk, or feature request. Include environment details and reproduction steps where relevant.
2. **Stay original** – Do not copy code or text from CIS, STIG, or vendor hardening content. Contributions must be original and legally clean.
3. **Create focused branches** – Fork the repo, create a feature branch named after the issue (e.g., `feature/firewall-profiles`), and keep commits small with descriptive messages.
4. **Coding standards** – Use Ansible best practices (idempotent tasks, defaults overridable via vars) and Python style enforced by `ruff`, `black`, and `bandit`. Shell scripts should pass `shellcheck`.
5. **Testing** – Before opening a pull request, run:
   ```bash
   scripts/lint.sh
   pytest
   molecule test
   ```
6. **Docs** – Update README, CHANGELOG, or role docs whenever behavior changes.
7. **Reviews** – Fill out the PR template, reference the issue, and describe the testing performed. Expect thorough reviews focused on security impact and idempotency.

By contributing you agree that your work will be licensed under the Apache License 2.0.
