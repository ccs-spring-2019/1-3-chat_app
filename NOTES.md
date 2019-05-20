## SQLite database

* a db.sqlite3 file is created the first time you run runserver or migrate.
* using runserver configures a database with Django's default settings
* using migrate will sync the database with the current state of any database models

## Activating Models

* makemigrations references all changes to the specified model (all if model name is not passed)
    * it's best practice to pass the app name; we want our makemigrations files to be as small and isolated as possible
* migrate executes the instructions in our migrations file

## Tests

* any function that has the word test at the beginning and exists in a tests.py file will be run when we execute the command python manage.py test

## Database Models null versus blank

* null=True sets NULL (versus NOT NULL) on the column in your DB
    * Blank values for Django field types such as DateTimeField or ForeignKey will be stored as NULL in the DB
* blank=True determines whether the field will be required in forms
    * If blank=True then the field will not be required, whereas if it's False the field cannot be blank
* The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. 
    * The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

## Foreign_Key

* allows for a many-to-one relationship
    * e.g. a given author can have many chats, but a chat can not have many authors
* Django provides a built-in User model that is used for authentication
* You must specify on on_delete option

## User Authentication

* Django installs the auth app, which provides a User object containing
    * username
    * password
    * email
    * first_name
    * last_name
* Django provides a default view for login and logout
* You'll have to create your own signup view

