#### Create a virtual environment named 'env' in the current directory. This environment is isolated from the global Python installation.
`python -m venv env`

#### Change the PowerShell execution policy to allow scripts to be run (necessary for activating the virtual environment on Windows).
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

#### Activate the virtual environment 'env'. This changes your shell to use the Python and pip executables within 'env' instead of the global installation.
`.\env\Scripts\activate`

#### Install the Python packages specified in the 'requirements.txt' file. This file lists all dependencies for a project.
`pip install -r requirements.txt`

#### List all the Python packages installed in the virtual environment. Useful for generating a 'requirements.txt' file.
`pip freeze`

#### Install the Django framework in the virtual environment. This command adds Django, allowing you to build and manage Django projects.
`pip install django`

#### Display the version of Django that is currently installed. This helps verify Django was installed successfully.
`python -m django --version`

#### Upgrade pip to the latest version. Keeping pip up-to-date ensures you can install the latest packages and security updates.
`python.exe -m pip install --upgrade pip`

#### Create a new Django project named 'mysite'. This sets up the initial structure of a Django project.
`django-admin startproject mysite`

#### Within the 'mysite' project, create a new Django application named 'blog'. Apps are modular components in Django.
`python manage.py startapp blog`

#### Apply migrations to the database. Migrations are Django's way of propagating changes made to models (adding a field, deleting a model, etc.) into the database schema.
`python manage.py makemigrations`
`python manage.py migrate`

#### Start the Django development server. By default, it runs on http://127.0.0.1:8000, allowing you to view your project in a web browser.
`python manage.py runserver`

#### Start the Django development server on a specific IP (127.0.0.1) and port (8001). Useful if you need to run multiple projects simultaneously or avoid port conflicts.
`python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings`

#### Creating a superuser
`python manage.py createsuperuser`