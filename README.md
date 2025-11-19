# 🛡️ Linux Hardening Blueprint for Small Business

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE) 
[![Tested Distros](https://img.shields.io/badge/tested-Debian%2012%20%E2%80%A2%20Ubuntu%2022.04%20%E2%80%A2%20Rocky%209-success.svg)](#-supported-distributions--поддерживаемые-дистрибутивы)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ansible 2.16+](https://img.shields.io/badge/ansible-2.16+-red.svg)](https://docs.ansible.com/)
[![CI](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/actions/workflows/ci.yml/badge.svg)](.github/workflows/ci.yml)

**Opinionated, automation-ready Linux hardening for small businesses and homelabs**

**Opinionated автоматизация усиления безопасности Linux для малого бизнеса и домашних лабораторий**

🎯 **Production-ready** | 🤖 **Ansible-based** | 🐧 **Multi-distro** | 🔒 **Security-First**

> ⚡ **[Quick Start](#-quick-start--быстрый-старт)** | 📖 **[Documentation](#-documentation--документация)** | 🔧 **[Profiles](#-profiles--профили)** | 🧪 **[Testing](#-testing--тестирование)** | 💼 **[Professional Services](#-production-deployment--professional-support)**

---

## 🎯 Production Deployment & Professional Support

Looking for **enterprise-grade security hardening** or **professional DevSecOps assistance**?

**[run-as-daemon.ru](https://run-as-daemon.ru)** — Professional DevOps & Security Services

**Services:**
- 🛡️ **Security Hardening**: Linux server hardening, compliance audits (CIS, DISA STIG)
- 🏗️ **Infrastructure Security**: Secure infrastructure design and implementation
- 🔒 **Security-First Architecture**: "Defense by design. Speed by default"
- ⚙️ **Automation**: Ansible, Terraform, CI/CD security integration
- 📊 **Compliance**: Readiness assessments, continuous compliance monitoring
- 🤖 **DevSecOps**: Managed security operations, incident response runbooks

💬 **Contact for consulting**: Available via Telegram, VK, WhatsApp, GitHub

---

## 🌟 Why This Blueprint Exists / Зачем этот проект

**English:**
Small teams rarely have dedicated security engineers, yet they still need a repeatable, defensible hardening story for auditors, customers, and their own peace of mind. This project packages safe defaults and pragmatic automation so freelancers and small businesses can deploy hardened hosts in hours instead of weeks.

**Русский:**
Небольшие команды редко имеют выделенных специалистов по безопасности, но им все равно нужна воспроизводимая и защищенная конфигурация для аудиторов, клиентов и собственного спокойствия. Этот проект предоставляет безопасные настройки по умолчанию и прагматичную автоматизацию, чтобы фрилансеры и малый бизнес могли развернуть защищенные хосты за часы, а не недели.

---

## ✨ Features / Возможности

### English:
- 🔐 **SSH Hardening**: Modern ciphers, key-based authentication, profile-aware policies
- 🛡️ **Firewall Management**: nftables/ufw with minimal, web, database-friendly rule sets
- 👥 **User & Sudo Control**: No passwordless sudo by default, access hygiene
- 📁 **Filesystem Security**: Sensible permissions, mount options hardening
- 🔄 **Auto Updates**: Automatic security updates with monitoring
- 📊 **Logging & Monitoring**: Attack-surface reduction, comprehensive audit trails
- 🎯 **Profile-Based**: workstation, server, hardened profiles with overrides
- 🐳 **Automation-Ready**: Ansible playbooks, idempotent, CI/CD friendly

### Русский:
- 🔐 **Усиление SSH**: Современные шифры, аутентификация по ключам, политики на основе профилей
- 🛡️ **Управление фаерволом**: nftables/ufw с готовыми наборами правил для минимальной, веб и database конфигураций
- 👥 **Контроль пользователей и sudo**: Без sudo без пароля по умолчанию, гигиена доступа
- 📁 **Безопасность файловой системы**: Разумные разрешения и параметры монтирования
- 🔄 **Автообновления**: Автоматические обновления безопасности с мониторингом
- 📊 **Логирование и мониторинг**: Уменьшение поверхности атаки, комплексные журналы аудита
- 🎯 **Профили**: рабочая станция, сервер, усиленная защита с возможностью переопределения
- 🐳 **Готовность к автоматизации**: Ansible playbooks, идемпотентность, интеграция с CI/CD

---

## 🐧 Supported Distributions / Поддерживаемые дистрибутивы

| Distribution | Version | Status | Notes |
|--------------|---------|--------|-------|
| Debian | 12 (Bookworm) | ✅ Tested | Recommended |
| Ubuntu | 22.04 LTS (Jammy) | ✅ Tested | LTS Support |
| Rocky Linux | 9 | ✅ Tested | RHEL Compatible |
| AlmaLinux | 9 | ✅ Tested | RHEL Compatible |

---

## 🏗️ Architecture / Архитектура

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

### English:
- **Inventories** live under `ansible/inventories/`
- **Group defaults** in `ansible/group_vars/`
- **Profiles** map to playbooks (`workstation.yml`, `server.yml`, `hardened.yml`) that include the shared baseline
- Each role is idempotent and can be run independently or as part of a complete profile

### Русский:
- **Инвентари** находятся в `ansible/inventories/`
- **Групповые настройки по умолчанию** в `ansible/group_vars/`
- **Профили** соответствуют playbook'ам (`workstation.yml`, `server.yml`, `hardened.yml`), которые включают общий базовый уровень
- Каждая роль идемпотентна и может выполняться независимо или как часть полного профиля

---

## 🚀 Quick Start / Быстрый старт

### Requirements / Требования:
- Python 3.10+
- Ansible 2.16+
- SSH access to managed hosts / SSH доступ к управляемым хостам
- Collections: `community.general` and `ansible.posix` (installed automatically by `scripts/install.sh`)

### Three-Command Setup / Установка в три команды:

```bash
# Clone and install / Клонируйте и установите
git clone https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business.git
cd linux-hardening-blueprint-small-business
scripts/install.sh

# Run hardening / Запустите усиление защиты
linux-harden --profile server --inventory ansible/inventories/example_inventory.yml --limit webservers

# Check status / Проверьте статус
ansible-playbook -i ansible/inventories/example_inventory.yml ansible/playbooks/server.yml --check
```

### Usage Options / Варианты использования:

**CLI Wrapper / CLI обертка:**
```bash
# Basic usage / Базовое использование
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --limit webservers

# Dry run / Пробный запуск
linux-harden --profile hardened \
  --inventory ansible/inventories/example_inventory.yml \
  --check

# With overrides / С переопределениями
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --extra-vars @custom_vars.yml
```

**Raw Ansible Playbooks / Прямые Ansible Playbooks:**
```bash
ansible-playbook -i ansible/inventories/example_inventory.yml \
  ansible/playbooks/server.yml -l webservers
```

---

## 🎯 Profiles / Профили

| Feature | Workstation | Server | Hardened |
|---------|-------------|--------|----------|
| **SSH Password Auth** | ⚠️ Optional | ❌ Disabled | ❌ Disabled |
| **Firewall** | ✅ Basic | ✅ Standard | ✅✅ Strict |
| **Logging** | ⚠️ Basic | ✅ Standard | ✅✅ Verbose |
| **Kernel Hardening** | ⚠️ Minimal | ✅ Standard | ✅✅ Maximum |
| **Auto Updates** | ✅ Enabled | ✅ Enabled | ✅ Enabled |
| **Sudo Access** | ⚠️ Flexible | ✅ Controlled | ✅✅ Restricted |
| **Best For** | Laptops/Desktops | Web/App Servers | Internet-facing |

### Profile Descriptions / Описание профилей:

**Workstation / Рабочая станция:**
- **English**: Keeps laptops usable, but enforces SSH keys, firewall defaults, auto updates, and telemetry hygiene.
- **Русский**: Сохраняет удобство использования ноутбуков, но обеспечивает SSH ключи, настройки фаервола по умолчанию, автообновления и контроль телеметрии.

**Server / Сервер:**
- **English**: Balanced default for web/app/database nodes; disables password SSH by default, applies conservative filesystem and sysctl settings.
- **Русский**: Сбалансированные настройки по умолчанию для веб/приложение/database узлов; отключает парольный SSH по умолчанию, применяет консервативные настройки файловой системы и sysctl.

**Hardened / Усиленная защита:**
- **English**: For exposed Internet hosts; enables stricter SSH and firewall rules, aggressive logging, and mount option tightening. Review before deploying to production workloads.
- **Русский**: Для хостов, открытых в Интернет; включает более строгие правила SSH и фаервола, агрессивное логирование и ужесточение опций монтирования. Проверьте перед развертыванием в продакшен.

**Customization / Настройка:**

Each profile extends the same roles with overridable variables (`ansible/group_vars/all.yml` and role defaults). You can mix and match roles or run a subset by editing playbooks.

Каждый профиль расширяет одни и те же роли с переопределяемыми переменными (`ansible/group_vars/all.yml` и значения по умолчанию ролей). Вы можете комбинировать роли или запускать подмножество, редактируя playbooks.

---

## 🧪 Testing / Тестирование

### Local Testing / Локальное тестирование:

```bash
# Unit tests / Модульные тесты
pytest tests/

# Linting / Проверка кода
scripts/lint.sh

# Molecule tests / Тесты Molecule
cd ansible
molecule test
```

### CI/CD Pipeline / CI/CD конвейер:

**English:**
- ✅ GitHub Actions automated testing
- ✅ Multi-distro matrix (Debian, Ubuntu, Rocky)
- ✅ Security scanning with pip-audit
- ✅ Idempotency checks

**Русский:**
- ✅ Автоматизированное тестирование GitHub Actions
- ✅ Матрица нескольких дистрибутивов (Debian, Ubuntu, Rocky)
- ✅ Сканирование безопасности с pip-audit
- ✅ Проверки идемпотентности

### Test Coverage / Покрытие тестами:

- **Unit tests** (`pytest`): CLI command builder and config schema validation
- **Molecule** (Docker driver): Ansible roles validation against Debian and Rocky images
- **GitHub Actions CI** (`.github/workflows/ci.yml`): Linting, unit tests, and Molecule jobs
- **Security workflow** (`.github/workflows/security.yml`): Dependency audits with `pip-audit`

---

## 🐛 Troubleshooting / Решение проблем

### Common Issues / Частые проблемы:

#### SSH Access Denied After Hardening

**English:**
If you're locked out after SSH hardening:
1. Use console access (cloud provider console, KVM, physical access)
2. Check `/etc/ssh/sshd_config.bak` for the backup configuration
3. Review SSH logs: `journalctl -u sshd` or `/var/log/auth.log`
4. Verify key-based authentication is properly configured
5. Temporarily enable password auth if needed: `PasswordAuthentication yes`
6. Restart SSH: `systemctl restart sshd`

**Русский:**
Если вы заблокированы после усиления SSH:
1. Используйте консольный доступ (консоль облачного провайдера, KVM, физический доступ)
2. Проверьте `/etc/ssh/sshd_config.bak` для резервной конфигурации
3. Просмотрите логи SSH: `journalctl -u sshd` или `/var/log/auth.log`
4. Убедитесь, что аутентификация по ключам правильно настроена
5. Временно включите парольную аутентификацию при необходимости: `PasswordAuthentication yes`
6. Перезапустите SSH: `systemctl restart sshd`

#### Firewall Blocks Legitimate Traffic

**English:**
If your firewall is blocking legitimate traffic:
1. Check active rules: `nft list ruleset` or `ufw status verbose`
2. Review firewall role variables in `ansible/group_vars/`
3. Add custom rules via overrides in your inventory or extra vars
4. Temporarily disable to test: `systemctl stop nftables` or `ufw disable`
5. Re-run playbook with corrected firewall settings

**Русский:**
Если ваш фаервол блокирует легитимный трафик:
1. Проверьте активные правила: `nft list ruleset` или `ufw status verbose`
2. Просмотрите переменные роли фаервола в `ansible/group_vars/`
3. Добавьте пользовательские правила через переопределения в вашем инвентаре или extra vars
4. Временно отключите для тестирования: `systemctl stop nftables` или `ufw disable`
5. Повторно запустите playbook с исправленными настройками фаервола

#### Auto-updates Not Working

**English:**
Verify unattended-upgrades service:
```bash
systemctl status unattended-upgrades
cat /var/log/unattended-upgrades/unattended-upgrades.log
apt-config dump APT::Periodic::Unattended-Upgrade  # Debian/Ubuntu
```

**Русский:**
Проверьте службу unattended-upgrades:
```bash
systemctl status unattended-upgrades
cat /var/log/unattended-upgrades/unattended-upgrades.log
apt-config dump APT::Periodic::Unattended-Upgrade  # Debian/Ubuntu
```

#### Playbook Fails on Specific Task

**English:**
- Run with verbose output: `ansible-playbook ... -vvv`
- Check role defaults and variables in `ansible/roles/*/defaults/main.yml`
- Review task conditions and when clauses
- Ensure target system meets distribution requirements

**Русский:**
- Запустите с подробным выводом: `ansible-playbook ... -vvv`
- Проверьте значения по умолчанию ролей и переменные в `ansible/roles/*/defaults/main.yml`
- Просмотрите условия задач и when клаузы
- Убедитесь, что целевая система соответствует требованиям дистрибутива

---

## 🔒 Security Considerations / Вопросы безопасности

⚠️ **Important / Важно**:

### English:
- This blueprint is **NOT** an official CIS, DISA STIG, or vendor benchmark
- Always test in **staging environments** before production deployment
- Maintain **backups** before applying changes (configs are backed up to `.bak` files)
- **Validate** against your specific compliance requirements
- Use at your **own risk** in production environments
- This is written from scratch based on **widely accepted best practices**
- You must validate the output against your own **compliance obligations**, **threat model**, and **change management** processes

### Русский:
- Этот проект **НЕ** является официальным CIS, DISA STIG или вендорным бенчмарком
- Всегда тестируйте на **тестовом окружении** перед развертыванием в продакшене
- Создавайте **резервные копии** перед применением изменений (конфиги резервируются в `.bak` файлы)
- **Проверяйте** соответствие вашим специфическим требованиям compliance
- Используйте на **свой риск** в продакшн окружении
- Проект написан с нуля на основе **широко признанных лучших практик**
- Вы должны проверить результат на соответствие вашим **обязательствам по compliance**, **модели угроз** и процессам **управления изменениями**

### Safety & Rollback / Безопасность и откат:

**English:**
- Every role is **idempotent**: running twice should yield zero changes
- Test on **staging VMs** or disposable cloud nodes before touching production
- **Backup** configs such as `/etc/ssh/sshd_config` (SSH hardening role creates `.bak` files automatically)
- To **revert** specific changes: disable the corresponding role in a playbook or override the relevant variables, then re-run the play

**Русский:**
- Каждая роль **идемпотентна**: повторный запуск не должен вносить изменений
- Тестируйте на **тестовых VM** или одноразовых облачных узлах перед продакшеном
- **Резервируйте** конфиги такие как `/etc/ssh/sshd_config` (роль SSH автоматически создает `.bak` файлы)
- Для **отката** конкретных изменений: отключите соответствующую роль в playbook или переопределите соответствующие переменные, затем повторно запустите play

---

## 📚 Documentation / Документация

- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - Contribution guidelines / Руководство по участию
- **[LEGAL.md](./LEGAL.md)** - Legal disclaimers and responsible use / Юридические оговорки и ответственное использование
- **[CHANGELOG.md](./CHANGELOG.md)** - Version history / История версий
- **[Ansible Roles](./ansible/roles/)** - Individual role documentation / Документация отдельных ролей
- **[CLI Documentation](./cli/)** - CLI wrapper documentation / Документация CLI обертки

---

## 👨‍💻 Author & Professional Services

**Ранас М. (Ranas M.)** — DevOps Engineer & Security Specialist

### 🌐 Professional Services: [run-as-daemon.ru](https://run-as-daemon.ru)

**"Defense by design. Speed by default"** — Security-first architecture with performance optimization

#### 💼 Services Offered:

**🛡️ Security & Hardening**
- Linux server security audits and hardening
- Compliance assessments (CIS, DISA STIG, PCI DSS)
- Security automation with Ansible
- Intrusion detection and prevention setup
- Security monitoring and alerting

**🏗️ Infrastructure & Orchestration**
- Secure infrastructure design
- Docker, Kubernetes, Nomad deployments
- High-availability cluster configuration
- CI/CD pipeline security integration

**🔒 DevSecOps Services**
- Security-first development workflows
- Automated security testing
- Vulnerability management
- Incident response planning
- Continuous compliance monitoring

**⚙️ Linux Administration**
- Server installation and configuration
- Firewall setup (nftables, ufw, iptables)
- SSH and VPN hardening
- Automated backups and disaster recovery

#### 📞 Contact for Consulting:
- 🌐 Website: [run-as-daemon.ru](https://run-as-daemon.ru)
- 💬 Telegram: Contact via website
- 📱 VK: Contact via website
- 💼 WhatsApp: Contact via website
- 🐙 GitHub: [@ranas-mukminov](https://github.com/ranas-mukminov)

---

## 📮 Support / Поддержка

### Community Support / Поддержка сообщества:

**English:**
- Open an issue on [GitHub Issues](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/issues)
- Check existing issues for solutions
- Review documentation in repository

**Русский:**
- Откройте issue на [GitHub Issues](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/issues)
- Проверьте существующие issues для решений
- Просмотрите документацию в репозитории

### Professional Support / Профессиональная поддержка:

**English:**
- Security audits and assessments
- Custom hardening implementations
- Compliance consulting
- Managed security operations
- 24/7 monitoring and incident response

**Русский:**
- Аудиты и оценка безопасности
- Кастомные реализации усиления защиты
- Консалтинг по compliance
- Управляемые операции безопасности
- Мониторинг и реагирование на инциденты 24/7

**Contact / Контакты:** [run-as-daemon.ru](https://run-as-daemon.ru)

---

## 🤝 Contributing / Участие в разработке

**English:**
We gladly accept issues and pull requests:
1. Open an issue describing the desired feature or bug fix
2. Fork the repository, create a topic branch, and keep commits small
3. Run `scripts/lint.sh`, `pytest`, and `molecule test` before submitting
4. Fill out the PR template and describe testing performed
5. See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines

**Русский:**
Мы с радостью принимаем issues и pull request'ы:
1. Откройте issue с описанием желаемой функции или исправления ошибки
2. Сделайте fork репозитория, создайте тематическую ветку и делайте небольшие коммиты
3. Запустите `scripts/lint.sh`, `pytest` и `molecule test` перед отправкой
4. Заполните шаблон PR и опишите проведенное тестирование
5. См. [CONTRIBUTING.md](./CONTRIBUTING.md) для подробных рекомендаций

---

## 📄 License / Лицензия

Licensed under the [Apache License 2.0](LICENSE).

By contributing you agree that your work will be licensed under the Apache License 2.0.

Лицензировано под [Apache License 2.0](LICENSE).

Внося вклад, вы соглашаетесь с тем, что ваша работа будет лицензирована под Apache License 2.0.

---

**Made with ❤️ for Small Business Security**

**Создано с ❤️ для безопасности малого бизнеса**

**Professional DevOps & Security Services:** [run-as-daemon.ru](https://run-as-daemon.ru)
