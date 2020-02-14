# CruiseX
This is a simulation of a Cruise Excursion API with CRUD options, optimized using sql queries rather than ORM.


## Instuctions
 - Clone repo 
 - Navigate into the root directory and run `pip install -r requirements.txt` via the Terminal
 - Edit the DATABASE in the _settings.py_ file
 - run `python manage.py makemigrations` then `python mannage.py migrate` to move all data tables to your        database.
 - Create a superuser `python manage.py createsuperuser`
 - run `python manage.py runserver`
 - Test your endpoints
 