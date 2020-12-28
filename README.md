## Cyber Security Base 2020 - Project repository

This repository contains my project in [Cyber Security Base 2020](https://cybersecuritybase.mooc.fi/module-3.1) -course in University of Helsinki. The purpose of this application is to figure out some cyber security flaws that such an app is possible to have.

**WARNING! This application contains security flaws ON PURPOSE!**

## Installation

Nothing special here, if you've completed part 2 of Cyber Security Base 2020 -course. Clone the repository, navigate to *flaws/* and run: ```python3 manage.py runserver```

Django server shall start and you'll find app in [localhost:8000](localhost:8000/).

Application has two users:
- alice:redqueen
- bob:squarepants

## Usage

App, named Inventory, is simple database application to store info about roleplay characters and their epic armor and weapons (both counted just items).

- Login with any of given users.
- At front page you'll see users characters and are able to create a new one.
- You'll also see latest item added by anyone.
- Click bottom link to see all items and to add a new one. Items-page contains simple list of all items in Inventory.
- At front page, click name of the character to see their details: name, level and items they have.
- At character page you are able to add item from Inventory to this specific character.

## Security flaws in app

As instructed, app contains five security flaws from [OWASP top ten list](https://owasp.org/www-project-top-ten/). These are:
- Broken Authentication
- Broken Access Control
- Security Misconfiguration
- Cross-Site-Scripting (XSS)
- Using components with Known Vulnerabilities