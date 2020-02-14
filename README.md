# CruiseX
This is a simulation of a Cruise Excursion API with CRUD options, optimized using sql queries rather than ORM.


## Instuctions
 - Clone repo 
 - Navigate into the root directory and run `pip install -r requirements.txt` via the Terminal
 - Edit the DATABASE in the _settings.py_ file
 - run `python manage.py makemigrations` then `python mannage.py migrate` to move all data tables to your        database.
 - Create a superuser `python manage.py createsuperuser`
 - `python manage.py loaddata data.json` to load default data into your db or you could proceed to testing the endpoints then add your own data
 - run `python manage.py runserver`
 - Test your endpoints.
    - Endpoints can be tested via the CLI or an API testing tool e.g POSTMAN
    - Get your access tokens via the `.../api/token/` url
    - Add tokens to request others 
    - List of url endpoints can be found in the Cruise/urls.py and CruiseAPI/urls.py.
    - Testing can also be done via the API doc-page[ core api] (`../api/doc/`)

 