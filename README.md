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

5. Install redis server on your operating system

7. Create settings_local.py with settings from settings_local_sample.py

8. Run `python manage.py migrate`

9. Start the development server and visit http://127.0.0.1:8000/

10. In new tab re activate the virtual enviroment to start celery worker::
    celery -A uploadshape worker --loglevel=info


11. Don't forget to write your google api key in settings_local.py file

12. Srid  of the shapefile must be 4326

This project use postgresql database
