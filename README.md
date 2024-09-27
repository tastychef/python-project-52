[![Hexlet Ltd. logo](https://beribuy.ru/uploads/blog-ck/59ece66cc0acd6a69b64bdbefeefab2f.webp)](https://ru.hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-package)

<h1 align="center">The Task Manager project</h1>

[![Actions Status](https://github.com/tastychef/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tastychef/python-project-52/actions)
[![Workflow status](https://github.com/tastychef/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tastychef/python-project-52/actions)

Это учебный проект курсов Хекслет.
Менеджер задач - это система управления задачами, похожая на http://www.redmine.org/. 

Она позволяет ставить задачи, назначать исполнителей и изменять их статусы. Для работы с системой требуется регистрация и аутентификация.
Проект основан на базе данных ***PostgreSQL/Sglite*** database, ***Django***, ***templating***, ***Bootstrap***, and ***Rollbar***.


Вы можете увидеть развернутое приложение на платформе Render [here](https://python-project-52-lsqu.onrender.com)

## Instalation
1. To install the project, please, clone the project from this repository, install poetry and install all dependencies:
```sh
git clone <package>
pip install poetry
make install
```
2. Please, define environment variables. Create .env file in the root of the project:
```sh
SECRET_KEY=''
DEBUG=False (True is the debugging mode)
RENDER_EXTERNAL_HOSTNAME='' (The external url in case the deploying on Render.com)
POST_SERVER_ITEM_ACCESS_TOKEN='' (For the error tracking service Rollbar.com)
```
3. To check the project's functionality, please, run the linter and tests:
```sh
make lint
make test
```