"""
Advanced session settings using django-user-sessions.

Ce module est importé uniquement quand DEBUG = False.
"""

# Backend de sessions : user_sessions (sessions liées au User)
SESSION_ENGINE = "user_sessions.backends.db"

# Durée de vie des cookies de session (en secondes)
# (complète / peut écraser la valeur de settings_security)
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14  # 14 jours

# Renouvelle la date d’expiration à chaque requête authentifiée
SESSION_SAVE_EVERY_REQUEST = True

# Optionnel : expirer la session à la fermeture du navigateur
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
