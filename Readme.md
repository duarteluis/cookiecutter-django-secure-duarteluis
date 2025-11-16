# **Cookiecutter Django Secure DUARTELUIS**

A fully hardened, production-ready Django project template featuring:

* **uv** for Python environment & dependency management
* **Django 5.x**, **PostgreSQL**, **Gunicorn**, **Nginx**
* **Celery + Redis/Valkey + Flower**
* **django-allauth** with **mandatory MFA (TOTP/WebAuthn)**
* **CustomUser model** from day zero
* **High-security defaults** (Argon2, CSP, HSTS, secure cookies, 2FA, session management)
* **pwned-passwords-django** + **django-pwned** password validation
* **django-user-sessions** (session revocation UI)
* **Pre-commit + Ruff** for code quality
* Modular settings and server bootstrap scripts
* Optional provisioning using **Fabric** or **Ansible**

This template is designed for **serious Django deployments**, internal platforms, SaaS, healthcare apps, or any project requiring strong authentication and secure defaults.

**For the moment, it's still in beta.**

---

## 🚀 Features

### **Security**

* Argon2 password hashing
* Strict CSP (Content Security Policy)
* HSTS, secure cookies, HTTPS-only
* Forced MFA via middleware
* Custom MFA adapter (issuer, labels)
* Session auditing + session revocation
* OWASP-compliant password validation
* Pwned-passwords check (HIBP API)
* django-axes login rate limiting
* Nginx login rate limiting (optional)

### **Development**

* uv virtual environment
* Ruff linting + formatting
* Pre-commit hooks clean by default
* Modular `settings/` structure
* A clean `apps/` package layout
* Cookiecutter prompts for DB settings, domain, broker backend, etc.

### **Server tooling (optional)**

* `server-setup/` provisioning scripts
* Fabric remote bootstrap
* Ansible roles for full reproducible infra

---

## 📦 Installation

### **1. Install Cookiecutter**

```bash
pip install cookiecutter
```

### **2. Generate your project**

```bash
cookiecutter https://github.com/<your-github>/cookiecutter-django-secure-duarteluis.git
```

You will be prompted for:

* project name
* project slug
* domain name
* Python version
* PostgreSQL settings
* Cache/Broker backend (redis/valkey/none)
* Celery & Flower options

---

## 🧱 Project Structure

```
{{project_slug}}/
│
├─ pyproject.toml
├─ manage.py
├─ .env.example
├─ .pre-commit-config.yaml
├─ ruff.toml
│
├─ {{project_slug}}/
│   ├─ settings.py
│   ├─ settings_security.py
│   ├─ settings_csp.py
│   ├─ settings_sessions.py
│   ├─ urls.py
│   ├─ wsgi.py
│   └─ celery.py
│
├─ apps/
│   └─ accounts/
│       ├─ models.py
│       ├─ forms.py
│       ├─ adapter.py
│       ├─ mfa_adapter.py
│       ├─ middleware.py
│       ├─ views/
│       ├─ urls/
│       └─ templates/
│
├─ templates/
│   ├─ base.html
│   └─ account/
│       ├─ login.html
│       ├─ signup.html
│       ├─ logout.html
│       ├─ password_reset*.html
│       └─ email/
│
└─ tools/
    └─ generate_secret_key.py
```

---

## 🛠 Development Setup

### **1. Create environment**

```bash
uv venv
uv pip install -e .[dev]
```

### **2. Pre-commit**

```bash
pre-commit install
```

### **3. Migrations**

```bash
uv run python manage.py migrate
```

### **4. Run server**

```bash
uv run python manage.py runserver
```

---

## 🔐 Environment Variables

Copy `.env.example`:

```bash
cp .env.example .env
```

Set:

```
DJANGO_SECRET_KEY=...
DJANGO_DEBUG=false
DJANGO_ALLOWED_HOSTS=yourdomain.com
DJANGO_DB_NAME=...
DJANGO_DB_USER=...
DJANGO_DB_PASSWORD=...
```

You can generate a secure key:

```bash
uv run python tools/generate_secret_key.py
```

---

## ⚙️ Optional: Celery / Flower

Celery worker:

```bash
uv run celery -A {{project_slug}} worker -l info
```

Celery beat scheduler:

```bash
uv run celery -A {{project_slug}} beat -l info
```

Flower monitoring:

```bash
uv run celery -A {{project_slug}} flower --port=5555
```

---

## 🔧 Optional: Server Deployment

### **Fabric**

```bash
uv pip install fabric paramiko pyyaml
uv run python remote_bootstrap.py
```

This will:

* connect to your server
* upload provisioning scripts
* run bootstrap (system packages, uv, PostgreSQL, Valkey/Redis, Nginx, Gunicorn, Certbot)

### **Ansible**

You also get a minimal playbook:

```bash
ansible-playbook -i inventory.ini site.yml
```

---

## 🛡 Security Summary

This template includes:

* Multi-factor authentication enforcement
* Mandatory email verification
* Secure session backend (user_sessions)
* Argon2 hashing
* CSP lockdown
* HSTS with preload
* Nginx rate limiting
* Axes login throttling
* Password breach detection
* Strict cookie policies
* Automatic onboarding workflow
* Session revocation UI

This exceeds the OWASP ASVS Level 2 baseline.

---

## 🧪 Recommended Next Steps

* Add CI (GitHub Actions)
* Define deployment pipelines
* Lock down Nginx rate limiting rules
* Configure HTTPS certificates for production
* Add monitoring (Prometheus / Loki / Grafana)

---

## 📄 License

You may add a license of your choice (MIT recommended).

---

## 👍 Need more?
Jus tell me what you need!