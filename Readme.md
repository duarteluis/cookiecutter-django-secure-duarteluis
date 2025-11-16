cookiecutter-django-secure/
├─ cookiecutter.json
├─ {{cookiecutter.project_slug}}/ ok
│  ├─ pyproject.toml ok
│  ├─ .env.example ok
│  ├─ .gitignore ok
│  ├─ .pre-commit-config.yaml ok
│  ├─ ruff.toml ok
│  ├─ manage.py ok
│  ├─ {{cookiecutter.project_slug}}/ ok
│  │   ├─ __init__.py ok
│  │   ├─ settings.py ok 
│  │   ├─ settings_security.py ok
│  │   ├─ settings_csp.py ok 
│  │   ├─ settings_sessions.py ok 
│  │   ├─ urls.py ok
│  │   ├─ wsgi.py ok
│  │   ├─ asgi.py ok
│  │   └─ celery.py ok
│  ├─ apps/ ok
│  │   └─ accounts/ ok
│  │       ├─ __init__.py ok
│  │       ├─ apps.py ok
│  │       ├─ models.py ok 
│  │       ├─ admin.py ok 
│  │       ├─ forms.py
│  │       ├─ adapter.py ok
│  │       ├─ mfa_adapter.py ok
│  │       ├─ middleware.py ok
│  │       ├─ views/ ok
│  │       │   ├─ profile.py ok 
│  │       │   ├─ onboarding.py ok 
│  │       │   └─ sessions.py ok
│  │       ├─ urls/
│  │       │   ├─ profile.py ok 
│  │       │   ├─ onboarding.py ok 
│  │       │   └─ sessions.py ok
│  │       └─ templates/ ok
│  │           ├─ account/ ok 
│  │           │   ├─ login.html ok
│  │           │   ├─ logout.html ok 
│  │           │   ├─ signup.html ok 
│  │           │   ├─ password_reset*.html / .txt ok
│  │           │   └─ email/… (confirmation, reset) ok
│  │           └─ accounts/ ok
│  │               ├─ profile.html ok
│  │               ├─ onboarding.html ok
│  │               └─ sessions/ ok
│  │                   ├─ list.html ok 
│  │                   └─ confirm_delete.html ok
│  ├─ templates/ ok
│  │   └─ base.html ok
│  └─ tools/
│      └─ generate_secret_key.py ok
└─ server-setup/            # tes scripts bash de provisioning serveur
   ├─ bootstrap_server.sh
   └─ modules/00_… 80_….
