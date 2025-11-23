# 🛡️ Linux Hardening Blueprint for Small Business

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Tested Distros](https://img.shields.io/badge/tested-Debian%2012%20%E2%80%A2%20Ubuntu%2022.04%20%E2%80%A2%20Rocky%209-success.svg)](#supported-distributions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ansible 2.16+](https://img.shields.io/badge/ansible-2.16+-red.svg)](https://docs.ansible.com/)
[![CI](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/actions/workflows/ci.yml/badge.svg)](.github/workflows/ci.yml)

🇬🇧 English | 🇷🇺 [Русская версия](README.ru.md)

**Production-ready Linux security hardening automation for small businesses, freelancers, and homelabs**

---

## Overview

Linux Hardening Blueprint is an opinionated, automation-first security hardening toolkit built with Ansible. It delivers repeatable, auditable server hardening for small teams without dedicated security engineers.

Package safe defaults and pragmatic automation to deploy hardened Linux hosts in hours instead of weeks. Choose from three profiles (workstation, server, hardened), customize via YAML, and apply changes idempotently via Ansible playbooks or a simple CLI wrapper.

Tested on Debian 12, Ubuntu 22.04 LTS, and Rocky Linux 9, with CI/CD validation, Molecule tests, and built-in rollback safety.

---

## Key Features

- 🔐 **SSH Hardening**: Modern ciphers, key-based auth, profile-aware policies
- 🛡️ **Firewall Management**: nftables/ufw with minimal, web, database-friendly rule sets
- 👥 **User & Sudo Control**: No passwordless sudo by default, access hygiene
- 📁 **Filesystem Security**: Sensible permissions, hardened mount options
- 🔄 **Automated Security Updates**: Unattended upgrades with monitoring
- 📊 **Comprehensive Logging**: Attack-surface reduction, audit trails
- 🎯 **Profile-Based**: workstation, server, hardened profiles with overrides
- 🐳 **Automation-Ready**: Ansible playbooks, idempotent, CI/CD friendly
- 🧪 **Battle-Tested**: pytest, Molecule integration tests, GitHub Actions CI

---

## Architecture

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

**Components:**
- **Inventories**: Target hosts at `ansible/inventories/`
- **Group Variables**: Defaults in `ansible/group_vars/all.yml`
- **Profiles**: Playbooks (`workstation.yml`, `server.yml`, `hardened.yml`)
- **Roles**: Modular Ansible roles (firewall, SSH, logging, etc.)
- **CLI Wrapper**: Python CLI (`linux-harden`) for simplified execution

---

## Requirements

**Supported Distributions:**

| Distribution | Version | Status |
|--------------|---------|--------|
| Debian       | 12 (Bookworm) | ✅ Tested |
| Ubuntu       | 22.04 LTS | ✅ Tested |
| Rocky Linux  | 9 | ✅ Tested |
| AlmaLinux    | 9 | ✅ Tested |

**Software:**
- Python 3.10+
- Ansible 2.16+
- SSH access to managed hosts with sudo
- Collections: `community.general`, `ansible.posix` (auto-installed)

**System:**
- Control node: 1 CPU, 512 MB RAM, 5 GB disk
- Target hosts: Root/sudo access, systemd

**Network:**
- SSH connectivity
- Internet access for packages
- Open required ports (22, 80, 443, etc.)

---

## Quick Start

```bash
# Clone and install
git clone https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business.git
cd linux-hardening-blueprint-small-business
scripts/install.sh
source .venv/bin/activate

# Configure inventory
# Edit ansible/inventories/example_inventory.yml

# Run hardening
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --limit webservers

# Verify (dry-run)
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --check
```

---

## Detailed Installation

### Debian 12 / Ubuntu 22.04 LTS

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git openssh-client

git clone https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business.git
cd linux-hardening-blueprint-small-business
scripts/install.sh
source .venv/bin/activate

linux-harden --version
ansible --version
```

### Rocky Linux 9 / AlmaLinux 9

```bash
sudo dnf install -y python3 python3-pip git openssh-clients

git clone https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business.git
cd linux-hardening-blueprint-small-business
scripts/install.sh
source .venv/bin/activate

linux-harden --version
ansible --version
```

---

## Configuration

### Main Config (`ansible/group_vars/all.yml`)

```yaml
linux_hardener_profile: server

linux_hardener_profiles:
  server:
    ssh_permit_root_login: "no"
    ssh_password_auth: false
    firewall_profile: web
    enforce_mount_options: true
    idle_timeout: 600

firewall_allowed_tcp_ports: [22, 80, 443]
logging_remote_host: ""
auto_update_reboot_strategy: if-needed
sudo_default_group: admin
```

### Override with Extra Vars

```bash
# Create custom_vars.yml
cat > custom_vars.yml <<EOF
firewall_allowed_tcp_ports: [22, 80, 443, 8080]
ssh_password_auth: false
idle_timeout: 300
logging_remote_host: "syslog.example.com:514"
EOF

# Apply
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --extra-vars @custom_vars.yml
```

### Firewall Profiles

- **minimal**: SSH only (22)
- **web**: SSH + HTTP/HTTPS (22, 80, 443)
- **database**: SSH + PostgreSQL/MySQL (22, 5432, 3306)
- **hardened_web**: Web + strict rate limiting

---

## Usage

### Manage Services

```bash
# SSH
sudo systemctl restart sshd
sudo systemctl status sshd

# Firewall (nftables)
sudo systemctl restart nftables
sudo nft list ruleset

# Firewall (ufw)
sudo ufw status verbose
sudo ufw reload

# Auto-updates
sudo systemctl status unattended-upgrades
```

### Common Tasks

```bash
# Run specific role
ansible-playbook -i ansible/inventories/example_inventory.yml \
  ansible/playbooks/server.yml --tags ssh_hardening

# Dry-run with diff
ansible-playbook -i ansible/inventories/example_inventory.yml \
  ansible/playbooks/server.yml --check --diff

# Verbose output
ansible-playbook -i ansible/inventories/example_inventory.yml \
  ansible/playbooks/server.yml -vvv
```

---

## Update / Upgrade

### Update Toolkit

```bash
cd linux-hardening-blueprint-small-business
git pull origin main
source .venv/bin/activate
pip install --upgrade -e ./cli
```

### Re-apply Hardening

```bash
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml
```

### Update Managed Hosts

Automatic updates enabled via `unattended-upgrades`. Manual:

```bash
# Debian/Ubuntu
sudo apt update && sudo apt upgrade -y

# Rocky/Alma
sudo dnf upgrade -y
```

---

## Logs and Troubleshooting

### Log Locations

```bash
# SSH logs
sudo journalctl -u sshd -f
sudo tail -f /var/log/auth.log  # Debian/Ubuntu
sudo tail -f /var/log/secure    # Rocky/Alma

# Firewall logs
sudo journalctl -k | grep nft
sudo tail -f /var/log/ufw.log

# Auto-updates
sudo tail -f /var/log/unattended-upgrades/unattended-upgrades.log
```

### Common Problems

**SSH Access Denied:**

1. Use console access (cloud console, KVM, physical)
2. Check backup: `/etc/ssh/sshd_config.bak`
3. Review logs: `journalctl -u sshd`
4. Verify SSH keys in `~/.ssh/authorized_keys`
5. Temp enable password auth:
   ```bash
   sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
   sudo systemctl restart sshd
   ```

**Firewall Blocks Traffic:**

1. Check rules: `sudo nft list ruleset` or `sudo ufw status verbose`
2. Review `firewall_allowed_tcp_ports` in config
3. Add ports to inventory or extra vars
4. Temp disable: `sudo systemctl stop nftables` or `sudo ufw disable`
5. Re-run with corrected settings

**Auto-Updates Not Working:**

```bash
sudo systemctl status unattended-upgrades
sudo cat /var/log/unattended-upgrades/unattended-upgrades.log
sudo unattended-upgrade --debug
```

**Playbook Fails:**

1. Run verbose: `ansible-playbook ... -vvv`
2. Check role defaults: `ansible/roles/*/defaults/main.yml`
3. Verify distribution requirements
4. Check Ansible version

---

## Security Considerations

### Important

- **NOT** official CIS/DISA STIG/vendor benchmark
- Always test in **staging** before production
- Maintain **backups** (configs auto-backed up to `.bak`)
- **Validate** against your compliance requirements
- Use at **own risk**
- Based on **widely accepted best practices**
- Validate against **threat model** and **change management**

### Safety & Rollback

- Every role is **idempotent**
- Test on staging VMs first
- Use `--check` for dry-run
- Configs backed up automatically
- Restore from `.bak` files if needed
- Override variables to revert changes

### Best Practices

**Before:**
1. Review role defaults
2. Customize firewall rules
3. Deploy SSH keys
4. Document changes
5. Schedule maintenance window

**After:**
1. Change default passwords
2. Restrict SSH access (VPN/firewall)
3. Configure remote logging
4. Enable monitoring
5. Regular security audits

**Do NOT:**
- Expose SSH to Internet without protection
- Disable all auth methods simultaneously
- Skip testing
- Ignore backups

---

## Project Structure

```
linux-hardening-blueprint-small-business/
├── ansible/
│   ├── inventories/      # Example inventories
│   ├── group_vars/       # Global defaults
│   ├── playbooks/        # Hardening playbooks
│   └── roles/            # Ansible roles
│       ├── firewall/
│       ├── logging/
│       ├── os_baseline/
│       ├── ssh_hardening/
│       ├── updates/
│       └── users_sudo/
├── cli/
│   └── linux_hardener/   # Python CLI wrapper
├── scripts/
│   ├── install.sh        # Installation script
│   ├── lint.sh           # Linting
│   └── run_playbook.sh
├── tests/
│   ├── unit/             # Pytest tests
│   └── integration/      # Molecule tests
├── .github/workflows/    # CI/CD
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Profiles

| Feature | Workstation | Server | Hardened |
|---------|-------------|--------|----------|
| **SSH Password** | ⚠️ Optional | ❌ Disabled | ❌ Disabled |
| **Firewall** | ✅ Basic | ✅ Standard | ✅✅ Strict |
| **Logging** | ⚠️ Basic | ✅ Standard | ✅✅ Verbose |
| **Kernel Hardening** | ⚠️ Minimal | ✅ Standard | ✅✅ Maximum |
| **Auto Updates** | ✅ Enabled | ✅ Enabled | ✅ Enabled |
| **Sudo** | ⚠️ Flexible | ✅ Controlled | ✅✅ Restricted |
| **Best For** | Laptops | Web/App Servers | Internet-facing |

**Workstation:** Developer laptops, desktops, admin jump boxes  
**Server:** Web/app/database nodes, private cloud  
**Hardened:** Internet-facing, DMZ, high-security

---

## Testing

```bash
# Unit tests
pytest tests/unit/

# Linting
scripts/lint.sh

# Molecule tests
cd tests/integration/molecule/default
molecule test
molecule test -- --limit debian12
```

**CI/CD:**
- ✅ GitHub Actions automated testing
- ✅ Multi-distro matrix (Debian, Ubuntu, Rocky)
- ✅ Security scanning (pip-audit, bandit)
- ✅ Idempotency checks

---

## Roadmap

- Additional distro support (Fedora, openSUSE)
- CIS benchmark compliance reporting
- Terraform/Packer integration
- Prometheus/Grafana integration
- Web-based management UI
- Container/Kubernetes hardening

See [GitHub Issues](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/issues).

---

## Contributing

1. Open an issue describing feature/bug
2. Fork repository, create topic branch
3. Keep commits small and descriptive
4. Run quality checks: `scripts/lint.sh`, `pytest`, `molecule test`
5. Fill out PR template
6. Ensure originality (no CIS/STIG copies)

See [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## License

Licensed under the [Apache License 2.0](LICENSE).

```
Copyright (c) 2025 Ranas Mukminov
```

By contributing you agree your work will be licensed under Apache License 2.0.

---

## Author and Commercial Support

**Author:** Ranas Mukminov ([@ranas-mukminov](https://github.com/ranas-mukminov))

### Professional Services: [run-as-daemon.ru](https://run-as-daemon.ru)

**"Defense by design. Speed by default"**

**Services:**

🛡️ **Security Hardening & Audits**
- Linux server hardening and compliance (CIS, DISA STIG, PCI DSS, HIPAA)
- Security automation (Ansible, Terraform)
- Intrusion detection setup

🏗️ **Infrastructure & Orchestration**
- Secure infrastructure design
- Docker, Kubernetes, Nomad deployments
- CI/CD security integration

🔒 **DevSecOps Services**
- Security-first workflows
- Continuous compliance monitoring
- Incident response planning

⚙️ **Linux Administration**
- Server configuration
- Firewall setup (nftables, ufw, iptables)
- Automated backups and DR

**Contact:**
- 🌐 [run-as-daemon.ru](https://run-as-daemon.ru)
- 🐙 [@ranas-mukminov](https://github.com/ranas-mukminov)
- 💬 Telegram/VK/WhatsApp via website

---

## Support

**Community:**
- [GitHub Issues](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/issues)

**Professional:**
- Security audits and assessments
- Custom hardening implementations
- Managed security operations
- 24/7 support with SLA

**Contact:** [run-as-daemon.ru](https://run-as-daemon.ru)

---

**Made with ❤️ for Small Business Security**

**Professional DevOps & Security Services:** [run-as-daemon.ru](https://run-as-daemon.ru)
