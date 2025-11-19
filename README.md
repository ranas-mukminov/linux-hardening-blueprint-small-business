# Linux Hardening Blueprint for Small Business

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE) [![Tested: Debian 12 / Ubuntu 22.04 / Rocky 9](https://img.shields.io/badge/tested-Debian%2012%20%E2%80%A2%20Ubuntu%2022.04%20%E2%80%A2%20Rocky%209-success.svg)](#supported-distributions) [![CI](https://github.com/run-as-daemon/linux-hardening-blueprint-small-business/actions/workflows/ci.yml/badge.svg)](.github/workflows/ci.yml)

**Opinionated, automation-ready Linux hardening for small businesses and homelabs.**

## Why this blueprint exists
Small teams rarely have dedicated security engineers, yet they still need a repeatable, defensible hardening story for auditors, customers, and their own peace of mind. This project packages safe defaults and pragmatic automation so freelancers and small businesses can deploy hardened hosts in hours instead of weeks.

## Features at a glance
- Hardened SSH with modern ciphers, access controls, and profile-aware auth policies
- nftables/ufw firewall blueprints with minimal, web, and database-friendly rule sets
- Local user, sudo, and service hygiene (no passwordless sudo by default)
- Sensible filesystem permissions, package hygiene, log rotation, and kernel/sysctl tweaks
- Auto security updates, time sync management, and attack-surface reduction for common daemons
- Profiles for `workstation`, `server`, and `hardened` use cases with overrides you can inspect and version control

## Supported distributions
- Debian 12 (Bookworm)
- Ubuntu 22.04 LTS (Jammy)
- Rocky Linux 9 / AlmaLinux 9

## Architecture overview
```
┌─────────────────────────────────────┐
│ Policies (YAML) + Profiles          │
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│ linux-harden CLI (Typer wrapper)    │
│  • Validates config schema          │
│  • Renders ansible-playbook command │
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│ Ansible Playbooks & Roles           │
│  • os_baseline, ssh_hardening,      │
│    firewall, logging, updates,      │
│    users_sudo                       │
└─────────────────────────────────────┘
```
- Inventories live under `ansible/inventories/`
- Group defaults in `ansible/group_vars/`
- Profiles map to playbooks (`workstation.yml`, `server.yml`, `hardened.yml`) that include the shared baseline

## Quick start
**Requirements**
- Python 3.10+
- Ansible 2.16+
- `ssh` access to managed hosts
- Collections: `community.general` and `ansible.posix` (installed automatically by `scripts/install.sh`)

**Clone & install tooling (optional helper script)**
```bash
git clone https://github.com/run-as-daemon/linux-hardening-blueprint-small-business.git
cd linux-hardening-blueprint-small-business
scripts/install.sh
```

**Run through CLI wrapper**
```bash
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --limit webservers
```
Add `--check` for dry runs, and `--extra-vars` to pass a YAML file with overrides.

**Run raw Ansible playbooks**
```bash
ansible-playbook -i ansible/inventories/example_inventory.yml \
  ansible/playbooks/server.yml -l webservers
```

## Profiles
- **workstation** – Keeps laptops usable, but enforces SSH keys, firewall defaults, auto updates, and telemetry hygiene.
- **server** – Balanced default for web/app/database nodes; disables password SSH by default, applies conservative fs/sysctl settings.
- **hardened** – For exposed Internet hosts; enables stricter SSH and firewall rules, aggressive logging, and mount option tightening. Review before deploying to production workloads.

Each profile extends the same roles with overridable variables (`ansible/group_vars/all.yml` and role defaults). You can mix and match roles or run a subset by editing playbooks.

## Safety, rollback, and operations
- Every role is idempotent: running twice should yield zero changes. `scripts/perf_check.sh` enforces this.
- Test on staging VMs or disposable cloud nodes before touching production.
- Maintain backups of configs such as `/etc/ssh/sshd_config` using version control (`ssh_hardening` role stores `.bak` files) or your own backup tooling.
- To revert specific changes, disable the corresponding role in a playbook or override the relevant variables, then re-run the play to converge back to the prior state.

## Security and compliance stance
This blueprint is **not** an official CIS, DISA STIG, or vendor benchmark implementation. It is written from scratch based on widely accepted best practices for SMB environments. You must validate the output against your own compliance obligations, threat model, and change management processes.

## Testing and CI
- Unit tests (`pytest`) cover the CLI command builder and config schema validation.
- Molecule (Docker driver) validates the Ansible roles against Debian and Rocky images.
- GitHub Actions CI (`.github/workflows/ci.yml`) runs linting (`scripts/lint.sh`), unit tests, and Molecule jobs across a distro matrix.
- Security workflow (`.github/workflows/security.yml`) executes dependency audits with `pip-audit`.

## Professional services by run-as-daemon.ru
[run-as-daemon.ru](https://run-as-daemon.ru) provides DevSecOps consulting focused on Linux hardening, automation, and continuous security operations for small and midsize teams. Commercial offerings include:
- Hardening readiness assessments and audits
- Custom implementation and tuning of this blueprint for mixed fleets
- Managed DevSecOps, including continuous compliance reports and incident-ready runbooks

Need white-glove support, training, or integration into existing CI/CD? Reach out via the site to engage the author.

## Legal and responsible use
- Defensive only: apply it on infrastructure you own or are contractually authorized to manage.
- No offensive features are included or planned.
- This repository deliberately avoids embedding copyrighted benchmark text.
- Nothing here is legal advice—consult your counsel for regulatory requirements.
- Review `LEGAL.md` for full disclaimers.

## Contributing
We gladly accept issues and pull requests:
1. Open an issue describing the desired feature or bug fix.
2. Fork, create a topic branch, and keep commits small.
3. Run `scripts/lint.sh`, `pytest`, and `molecule test` before submitting.
4. Fill out the PR template and describe testing performed.

## License
Licensed under the [Apache License 2.0](LICENSE).
