## Cyber Security Base 2020 - Project repository

This repository contains my project in [Cyber Security Base 2020](https://cybersecuritybase.mooc.fi/module-3.1) -course in University of Helsinki. The purpose of this application is to figure out some cyber security flaws that such an app is possible to have.

**WARNING! This application contains security flaws ON PURPOSE!**

## Installation

Nothing special here, if you've completed part 2 of Cyber Security Base 2020 -course. Clone the repository, navigate to *flaws/* and run: ```python3 manage.py runserver```

Django server shall start and you'll find app in [localhost:8000/inventory](localhost:8000/).

Application has two users:
- alice:redqueen
- bob:squarepants

## Security flaws in app

As instructed, app contains five security flaws from [OWASP top ten list](https://owasp.org/www-project-top-ten/). These are:
- Injection
- Broken Authentication
- Sensitive Data Exposure
- Broken Access Control
- Security Misconfiguration/Cross-Site Scripting