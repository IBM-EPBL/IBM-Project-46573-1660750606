[tool.poetry]
name = "python-template"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.8.0,<3.9"
numpy = "^1.22.2"
replit = "^3.2.4"
Flask = "^2.2.0"
urllib3 = "^1.26.12"
firebase = "^3.0.1"
requests = "^2.28.1"
Pyrebase4 = "^4.5.0"
wiotp-sdk = "^0.11.0"
hx711 = "^1.1.2"

[tool.poetry.dev-dependencies]
debugpy = "^1.6.2"
replit-python-lsp-server = {extras = ["yapf", "rope", "pyflakes"], version = "^1.5.9"}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
