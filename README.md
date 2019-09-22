# Nik

Project to keep professional profiles.

## Installation for development

* clone this repository
* Inside the nik directory, create a virtualenv. For example:
  `virtualenv --python=python3 .venv`
* Activate the virtualenv. For example:
  `source .venv/bin/activate`
* Set the required environment variables in a file. The
  required environment variables are the following:
  * NIK_DB_NAME: Name of your database.
  * NIK_DB_USERNAME: Name of the user of your PostgreSQL.
  * NIK_DB_PASSWORD: Password of the user of your PostgreSQL.
  * NIK_DB_HOST: Database host.
  * NIK_DB_PORT: Database port.
  
  For example: 
  ```buildoutcfg
  export NIK_DB_NAME="nik"
  export NIK_DB_USERNAME="my_username"
  export NIK_DB_PASSWORD="my_password"
  export NIK_DB_HOST="localhost"
  export NIK_DB_PORT="5432"
  ```

* Load the variables. For example: `source vars`

* Create the database. For example
  `createdb $NIK_DB_NAME -U $NIK_DB_USERNAME -W -h localhost`
  
* Install the requirements. `pip install -r requirements.txt`
  
* Run the first migrations:
  `python manage.py migrate`
  
* Test your server:
  `python manage.py runserver   `