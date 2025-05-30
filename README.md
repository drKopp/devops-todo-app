﻿# Mon projet DevOps


# ✅ DevOps To-Do App – Backend avec Flask

Ce projet est une **API To-Do List** simple développée avec **Flask** dans le but de pratiquer le développement backend, les tests et le linting dans un contexte DevOps.

---

## 📁 Contenu du dossier `backend/`

| Fichier                 | Description |
|------------------------|-------------|
| `app.py`               | Code principal de l'API Flask |
| `test_app.py`          | Tests unitaires et d'intégration de l'API |
| `requirements.txt`     | Dépendances nécessaires (Flask, pytest, etc.) |
| `lint_black.txt`       | Résultat du formatage avec Black |
| `lint_flake8.txt`      | Résultat de l’analyse statique avec Flake8 |
| `lint_isort.txt`       | Résultat du tri des imports avec isort |
| `lint_pylint.txt`      | Résultat de l’analyse statique avec pylint |

---

## 📦 Installation

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
