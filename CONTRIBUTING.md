# Contributing

This file contains information on how to contribute to the project.


## Environment Setup

The project runs on Python 3. To see if it's installed, try running `python3` in your terminal. To assist in managing the projects dependencies, we use [virtualenv][virtualenv] and [virtualenvwrapper][virtualenvwrapper]. We recommend installing them before continuing, and the rest of the setup guide will assume they are installed.

To set up the environment, create a virtual environment and install the project's requirements:

```shell
$ mkproject --python=python3 comp426-api
$ pip install -r requirements/base.txt
```


## Running the Development Server

While developing a new feature, you can test it out by running a local development server:

```shell
$ api/manage.py migrate
$ api/manage.py runserver
```

The development server will then be available at localhost:8000.


[virtualenv]: https://virtualenv.pypa.io/en/stable/installation/
[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/en/latest/install.html
