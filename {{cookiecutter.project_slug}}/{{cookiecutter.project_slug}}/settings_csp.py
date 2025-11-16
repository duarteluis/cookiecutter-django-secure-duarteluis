"""
Content Security Policy profile using django-csp.

Ce module est importé uniquement quand DEBUG = False.
"""

# Politique par défaut restrictive
CSP_DEFAULT_SRC = ("'self'",)

# Scripts : uniquement 'self' (pas d'inline)
CSP_SCRIPT_SRC = (
    "'self'",
)

# Styles : 'self' + 'unsafe-inline' (à durcir plus tard avec nonces / hashes)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
)

# Images
CSP_IMG_SRC = (
    "'self'",
    "data:",
)

# Fonts
CSP_FONT_SRC = (
    "'self'",
    "data:",
)

# Requêtes XHR / fetch
CSP_CONNECT_SRC = ("'self'",)

# Interdiction d’intégrer le site dans des iframes
CSP_FRAME_ANCESTORS = ("'none'",)

# Mode blocage (False) ; mettre True pour un mode report-only
CSP_REPORT_ONLY = False

# Optionnel : endpoint pour les rapports CSP
# CSP_REPORT_URI = "https://csp-report.example.com/report"
