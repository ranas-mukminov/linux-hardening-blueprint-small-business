# 🛡️ Linux Hardening Blueprint для малого бизнеса

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Tested Distros](https://img.shields.io/badge/tested-Debian%2012%20%E2%80%A2%20Ubuntu%2022.04%20%E2%80%A2%20Rocky%209-success.svg)](#поддерживаемые-дистрибутивы)
[![Python 3.10+](https://img shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ansible 2.16+](https://img.shields.io/badge/ansible-2.16+-red.svg)](https://docs.ansible.com/)
[![CI](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/actions/workflows/ci.yml/badge.svg)](.github/workflows/ci.yml)

🇷🇺 Русская версия | 🇬🇧 [English version](README.md)

**Готовая к продакшену автоматизация усиления безопасности Linux для малого бизнеса, фрилансеров и домашних лабораторий**

---

## Описание

Linux Hardening Blueprint — это комплексный инструмент автоматизации усиления безопасности на основе Ansible с готовыми решениями. Он обеспечивает воспроизводимую и проверяемую защиту серверов для небольших команд без выделенных специалистов по безопасности.

Пакет безопасных настроек по умолчанию и прагматичной автоматизации для развертывания защищенных хостов Linux за часы, а не недели. Выбирайте из трех профилей (workstation, server, hardened), настраивайте через YAML и применяйте изменения идемпотентно через Ansible playbooks или простой CLI wrapper.

Протестировано на Debian 12, Ubuntu 22.04 LTS и Rocky Linux 9 с валидацией через CI/CD, тестами Molecule и встроенной безопасностью отката.

---

## Основные возможности

- 🔐 **Усиление SSH**: Современные шифры, аутентификация по ключам, политики на основе профилей
- 🛡️ **Управление фаерволом**: nftables/ufw с готовыми наборами правил для минимальной, веб и database конфигураций
- 👥 **Контроль пользователей и sudo**: Без sudo без пароля по умолчанию, гигиена доступа
- 📁 **Безопасность файловой системы**: Разумные разрешения и параметры монтирования
- 🔄 **Автоматические обновления безопасности**: Unattended upgrades с мониторингом
- 📊 **Комплексное логирование**: Уменьшение поверхности атаки, журналы аудита
- 🎯 **Профили**: рабочая станция, сервер, усиленная защита с возможностью переопределения
- 🐳 **Готовность к автоматизации**: Ansible playbooks, идемпотентность, интеграция с CI/CD
- 🧪 **Протестировано в боевых условиях**: pytest, интеграционные тесты Molecule, GitHub Actions CI

---

## Архитектура

```
┌─────────────────────────────────────┐
│ Политики (YAML) + Профили           │
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│ linux-harden CLI (Typer wrapper)    │
│  • Валидация схемы конфигурации     │
│  • Генерация ansible-playbook       │
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│ Ansible Playbooks и Roles           │
│  • os_baseline, ssh_hardening,      │
│    firewall, logging, updates,      │
│    users_sudo                       │
└─────────────────────────────────────┘
```

**Компоненты:**
- **Инвентари**: Целевые хосты в `ansible/inventories/`
- **Групповые переменные**: Значения по умолчанию в `ansible/group_vars/all.yml`
- **Профили**: Playbooks (`workstation.yml`, `server.yml`, `hardened.yml`)
- **Roles**: Модульные Ansible роли (firewall, SSH, logging и т.д.)
- **CLI Wrapper**: Python CLI (`linux-harden`) для упрощенного выполнения

---

## Требования

**Поддерживаемые дистрибутивы:**

| Дистрибутив  | Версия         | Статус    |
|--------------|----------------|-----------|
| Debian       | 12 (Bookworm)  | ✅ Протестирован |
| Ubuntu       | 22.04 LTS      | ✅ Протестирован |
| Rocky Linux  | 9              | ✅ Протестирован |
| AlmaLinux    | 9              | ✅ Протестирован |

**Программное обеспечение:**
- Python 3.10+
- Ansible 2.16+
- SSH доступ к управляемым хостам с sudo
- Коллекции: `community.general`, `ansible.posix` (устанавливаются автоматически)

**Система:**
- Узел управления: 1 CPU, 512 МБ RAM, 5 ГБ диска
- Целевые хосты: Root/sudo доступ, systemd

**Сеть:**
- SSH подключение
- Доступ в Интернет для пакетов
- Открытые необходимые порты (22, 80, 443 и т.д.)

---

## Быстрый старт

```bash
# Клонировать и установить
git clone https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business.git
cd linux-hardening-blueprint-small-business
scripts/install.sh
source .venv/bin/activate

# Настроить инвентарь
# Редактировать ansible/inventories/example_inventory.yml

# Запустить усиление защиты
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --limit webservers

# Проверить (пробный запуск)
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --check
```

---

## Подробная установка

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

## Настройка

### Основной конфиг (`ansible/group_vars/all.yml`)

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

### Переопределение через Extra Vars

```bash
# Создать custom_vars.yml
cat > custom_vars.yml <<EOF
firewall_allowed_tcp_ports: [22, 80, 443, 8080]
ssh_password_auth: false
idle_timeout: 300
logging_remote_host: "syslog.example.com:514"
EOF

# Применить
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml \
  --extra-vars @custom_vars.yml
```

### Профили фаервола

- **minimal**: Только SSH (22)
- **web**: SSH + HTTP/HTTPS (22, 80, 443)
- **database**: SSH + PostgreSQL/MySQL (22, 5432, 3306)
- **hardened_web**: Web + строгое ограничение частоты запросов

---

## Использование

### Управление сервисами

```bash
# SSH
sudo systemctl restart sshd
sudo systemctl status sshd

# Фаервол (nftables)
sudo systemctl restart nftables
sudo nft list ruleset

# Фаервол (ufw)
sudo ufw status verbose
sudo ufw reload

# Автообновления
sudo systemctl status unattended-upgrades
```

### Типичные задачи

```bash
# Запустить конкретную роль
ansible-playbook -i ansible/inventories/example_inventory.yml \
  ansible/playbooks/server.yml --tags ssh_hardening

# Пробный запуск с diff
ansible-playbook -i ansible/inventories/example_inventory.yml \
  ansible/playbooks/server.yml --check --diff

# Подробный вывод
ansible-playbook -i ansible/inventories/example_inventory.yml \
  ansible/playbooks/server.yml -vvv
```

---

## Обновление

### Обновить инструментарий

```bash
cd linux-hardening-blueprint-small-business
git pull origin main
source .venv/bin/activate
pip install --upgrade -e ./cli
```

### Повторно применить усиление

```bash
linux-harden --profile server \
  --inventory ansible/inventories/example_inventory.yml
```

### Обновить управляемые хосты

Автоматические обновления включены через `unattended-upgrades`. Вручную:

```bash
# Debian/Ubuntu
sudo apt update && sudo apt upgrade -y

# Rocky/Alma
sudo dnf upgrade -y
```

---

## Логи и устранение неполадок

### Расположение логов

```bash
# Логи SSH
sudo journalctl -u sshd -f
sudo tail -f /var/log/auth.log  # Debian/Ubuntu
sudo tail -f /var/log/secure    # Rocky/Alma

# Логи фаервола
sudo journalctl -k | grep nft
sudo tail -f /var/log/ufw.log

# Логи автообновлений
sudo tail -f /var/log/unattended-upgrades/unattended-upgrades.log
```

### Частые проблемы

**SSH доступ запрещен:**

1. Используйте консольный доступ (консоль облачного провайдера, KVM, физический доступ)
2. Проверьте резервную копию: `/etc/ssh/sshd_config.bak`
3. Просмотрите логи: `journalctl -u sshd`
4. Проверьте SSH ключи в `~/.ssh/authorized_keys`
5. Временно включите парольную аутентификацию:
   ```bash
   sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
   sudo systemctl restart sshd
   ```

**Фаервол блокирует трафик:**

1. Проверьте правила: `sudo nft list ruleset` или `sudo ufw status verbose`
2. Просмотрите `firewall_allowed_tcp_ports` в конфигурации
3. Добавьте порты в инвентарь или extra vars
4. Временно отключите: `sudo systemctl stop nftables` или `sudo ufw disable`
5. Повторно запустите с исправленными настройками

**Автообновления не работают:**

```bash
sudo systemctl status unattended-upgrades
sudo cat /var/log/unattended-upgrades/unattended-upgrades.log
sudo unattended-upgrade --debug
```

**Playbook падает:**

1. Запустите с подробным выводом: `ansible-playbook ... -vvv`
2. Проверьте значения по умолчанию ролей: `ansible/roles/*/defaults/main.yml`
3. Проверьте требования дистрибутива
4. Проверьте версию Ansible

---

## Замечания по безопасности

### Важно

- **НЕ** является официальным CIS/DISA STIG/вендорным бенчмарком
- Всегда тестируйте на **тестовом окружении** перед продакшеном
- Создавайте **резервные копии** (конфиги автоматически резервируются в `.bak`)
- **Проверяйте** соответствие вашим требованиям compliance
- Используйте на **свой риск**
- Основано на **широко признанных лучших практиках**
- Проверьте на соответствие вашей **модели угроз** и процессам **управления изменениями**

### Безопасность и откат

- Каждая роль **идемпотентна**
- Тестируйте на тестовых VM сначала
- Используйте `--check` для пробного запуска
- Конфиги резервируются автоматически
- Восстановление из `.bak` файлов при необходимости
- Переопределите переменные для отката изменений

### Лучшие практики

**До развертывания:**
1. Просмотрите значения по умолчанию ролей
2. Настройте правила фаервола
3. Разверните SSH ключи
4. Задокументируйте изменения
5. Запланируйте окно обслуживания

**После развертывания:**
1. Смените пароли по умолчанию
2. Ограничьте доступ SSH (VPN/фаервол)
3. Настройте удаленное логирование
4. Включите мониторинг
5. Регулярные аудиты безопасности

**НЕ делайте:**
- Не выставляйте SSH в Интернет без защиты
- Не отключайте все методы аутентификации одновременно
- Не пропускайте тестирование
- Не игнорируйте резервные копии

---

## Структура проекта

```
linux-hardening-blueprint-small-business/
├── ansible/
│   ├── inventories/      # Примеры инвентарей
│   ├── group_vars/       # Глобальные настройки по умолчанию
│   ├── playbooks/        # Playbooks усиления защиты
│   └── roles/            # Ansible роли
│       ├── firewall/
│       ├── logging/
│       ├── os_baseline/
│       ├── ssh_hardening/
│       ├── updates/
│       └── users_sudo/
├── cli/
│   └── linux_hardener/   # Python CLI wrapper
├── scripts/
│   ├── install.sh        # Скрипт установки
│   ├── lint.sh           # Линтинг
│   └── run_playbook.sh
├── tests/
│   ├── unit/             # Pytest тесты
│   └── integration/      # Molecule тесты
├── .github/workflows/    # CI/CD
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Профили

| Функция | Workstation | Server | Hardened |
|---------|-------------|--------|----------|
| **SSH пароль** | ⚠️ По желанию | ❌ Отключен | ❌ Отключен |
| **Фаервол** | ✅ Базовый | ✅ Стандартный | ✅✅ Строгий |
| **Логирование** | ⚠️ Базовое | ✅ Стандартное | ✅✅ Подробное |
| **Усиление ядра** | ⚠️ Минимальное | ✅ Стандартное | ✅✅ Максимальное |
| **Автообновления** | ✅ Включены | ✅ Включены | ✅ Включены |
| **Sudo** | ⚠️ Гибкий | ✅ Контролируемый | ✅✅ Ограниченный |
| **Лучше для** | Ноутбуки | Веб/App серверы | Внешние хосты |

**Workstation:** Ноутбуки разработчиков, десктопы, jump-боксы  
**Server:** Веб/приложения/БД узлы, частное облако  
**Hardened:** Хосты в Интернете, DMZ, высокая безопасность

---

## Тестирование

```bash
# Модульные тесты
pytest tests/unit/

# Линтинг
scripts/lint.sh

# Тесты Molecule
cd tests/integration/molecule/default
molecule test
molecule test -- --limit debian12
```

**CI/CD:**
- ✅ Автоматизированное тестирование GitHub Actions
- ✅ Матрица нескольких дистрибутивов (Debian, Ubuntu, Rocky)
- ✅ Сканирование безопасности (pip-audit, bandit)
- ✅ Проверки идемпотентности

---

## Планы развития

- Поддержка дополнительных дистрибутивов (Fedora, openSUSE)
- Отчеты о соответствии CIS benchmark
- Интеграция с Terraform/Packer
- Интеграция с Prometheus/Grafana
- Web-интерфейс управления
- Усиление контейнеров/Kubernetes

См. [GitHub Issues](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/issues).

---

## Как внести вклад

1. Откройте issue с описанием функции/ошибки
2. Сделайте fork репозитория, создайте тематическую ветку
3. Делайте небольшие и понятные коммиты
4. Запустите проверки качества: `scripts/lint.sh`, `pytest`, `molecule test`
5. Заполните шаблон PR
6. Обеспечьте оригинальность (без копий CIS/STIG)

См. [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## Лицензия

Лицензировано под [Apache License 2.0](LICENSE).

```
Copyright (c) 2025 Ranas Mukminov
```

Внося вклад, вы соглашаетесь с тем, что ваша работа будет лицензирована под Apache License 2.0.

---

## Автор и коммерческая поддержка

**Автор:** Ранас Мукминов ([@ranas-mukminov](https://github.com/ranas-mukminov))

### Профессиональные услуги: [run-as-daemon.ru](https://run-as-daemon.ru)

**"Защита по дизайну. Скорость по умолчанию"**

**Услуги:**

🛡️ **Усиление безопасности и аудиты**
- Усиление безопасности Linux серверов и compliance (CIS, DISA STIG, PCI DSS, HIPAA)
- Автоматизация безопасности (Ansible, Terraform)
- Настройка систем обнаружения вторжений

🏗️ **Инфраструктура и оркестрация**
- Проектирование безопасной инфраструктуры
- Развертывание Docker, Kubernetes, Nomad
- Интеграция безопасности в CI/CD

🔒 **DevSecOps услуги**
- Рабочие процессы с приоритетом безопасности
- Непрерывный мониторинг compliance
- Планирование реагирования на инциденты

⚙️ **Администрирование Linux**
- Настройка серверов
- Настройка фаервола (nftables, ufw, iptables)
- Автоматизированные резервные копии и DR

**Контакты:**
- 🌐 [run-as-daemon.ru](https://run-as-daemon.ru)
- 🐙 [@ranas-mukminov](https://github.com/ranas-mukminov)
- 💬 Telegram/VK/WhatsApp через сайт

---

## Поддержка

**Поддержка сообщества:**
- [GitHub Issues](https://github.com/ranas-mukminov/linux-hardening-blueprint-small-business/issues)

**Профессиональная поддержка:**
- Аудиты и оценка безопасности
- Кастомные внедрения усиления защиты
- Управляемые операции безопасности
- Поддержка 24/7 с SLA

**Контакты:** [run-as-daemon.ru](https://run-as-daemon.ru)

---

**Создано с ❤️ для безопасности малого бизнеса**

**Профессиональные DevOps и услуги безопасности:** [run-as-daemon.ru](https://run-as-daemon.ru)
