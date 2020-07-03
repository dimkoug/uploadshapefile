# uploadshape
Geodjango project to upload shape files.

Quick start
-----------

1. Clone repo  like this::

      git clone  https://github.com/dimkoug/uploadshape.git

2. Create a virtualenv::

    python3 -m venv virtualenv

3. Activate virtualenv

4. Install packages from requirements.txt file

5. Create settings_local.py with settings from settings_local_sample.py

6. Run `python manage.py migrate`

7. Start the development server and visit http://127.0.0.1:8000/

8. In new tab re activate the virtual enviroment to start celery worker::
    celery -A uploadshape worker --loglevel=info


9. Don't forget to write your google api key in settings_local.py file


This project use postgresql database
