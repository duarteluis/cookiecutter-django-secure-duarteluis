"""
Security profile for production deployments.

Ce module est importé uniquement quand DEBUG = False.
"""

# 1) Hashage des mots de passe : Argon2 en premier
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# 2) HTTPS et redirections
SECURE_SSL_REDIRECT = True

# 3) Cookies durcis
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
# Garder False si tu utilises le token CSRF dans le DOM ou via JS
CSRF_COOKIE_HTTPONLY = False

# 4) Headers de sécurité
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# 5) HSTS (à activer seulement quand tout le site est en HTTPS)
SECURE_HSTS_SECONDS = 31536000  # 1 an
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 6) Durée de vie des sessions (complément de settings_sessions)
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14  # 14 jours

# 7) CSRF trusted origins (à ajuster par environnement)
# CSRF_TRUSTED_ORIGINS = [
#     "https://{{ cookiecutter.domain_name }}",
# ]
