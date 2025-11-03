# PESEL Checker 

A small Django app to validate PESEL and show information in it.

## Installation 

Prerequisites
- Python 3.12
- Pipenv

```powershell
pipenv install --dev
pipenv run python -m playwright install
pipenv shell
```

Set up the Django project

```powershell
python manage.py migrate
python manage.py runserver
```