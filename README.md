# Gemini – Django Chat Interface

> A modern, responsive chat interface powered by Django and Bootstrap 5, built for clarity, speed, and extensibility.

Gemini is a production‑ready foundation for conversational web experiences. It centralizes layout, assets, and UX patterns in a shared base template to ensure consistency, accessibility, and rapid iteration across pages. With CSRF‑protected forms, clean Bootstrap components, and a clear separation of concerns, the project is ideal for building assistants, knowledge bots, or Q&A tools—while remaining easy to brand, extend, and deploy.

## Features

- Modern, responsive UI using Bootstrap 5
- Shared base layout to keep templates clean and DRY
- Simple chat form with CSRF protection
- Extensible structure for adding new pages and features

## Environment Variables

Set the following environment variables before running the app (via your shell, process manager, or your hosting provider’s dashboard). Do not commit secrets to version control.

Required/common variables:
- SECRET_KEY: A long, random string used by Django for cryptographic signing (required).
- DEBUG: true/false (use False in production).
- ALLOWED_HOSTS: Comma‑separated list of allowed hosts (e.g., 127.0.0.1,localhost).
- GEMINI_API_KEY or other provider keys your features require (if applicable).

Examples (shell):

macOS/Linux:

- Python 3.13+
- Django
- Bootstrap 5 (via CDN)

## Prerequisites

- Python 3.13+ installed
- Virtual environments available (recommended)
- Git (optional but recommended)

## Quick Start

1) Clone the repository
# Ai_Assistant
