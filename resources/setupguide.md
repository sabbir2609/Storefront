# Environment setup guide for the project. [on WSL2]

## Use pipenv to install the dependencies

`pipenv install -r requirements.txt`

## Database setup

### Install postgresql and redis

**To install PostgreSQL on WSL (ie. Ubuntu):**

1. Open your WSL terminal (ie. Ubuntu).
2. Update your Ubuntu packages: `sudo apt update`
3. Once the packages have updated, install PostgreSQL (and the -contrib package which has some helpful utilities) with: `sudo apt install postgresql postgresql-contrib`
4. Confirm installation and get the version number: `psql --version`

### There are 3 commands you need to know once PostgreSQL is installed:

1. `sudo service postgresql status` - for checking the status of your database.
2. `sudo service postgresql start` - to start running your database.
3. `sudo service postgresql stop` - to stop running your database.

**The default admin user, `postgres`, needs a password assigned in order to connect to a database.** 

## To set a password:

Enter the command: `sudo passwd postgres`
You will get a prompt to enter your new password.
Close and reopen your terminal.

## To create a new database:    

1. Enter the command: `sudo -u postgres psql`
2. You will be prompted to enter your password.
3. Once you are logged in, you can create a new database with the command: `CREATE DATABASE <database_name>;`
4. You can check that the database was created by running the command: `\l`
5. You can exit the PostgreSQL prompt by running the command: `\q`

## change password for postgres user

1. run `sudo -u postgres psql`
2. `postgres=# \password postgres`
3. enter new password
4. `postgres=# \q`


## Setup redis:

**To install Redis on WSL (ie. Ubuntu):**

1. Open your WSL terminal (ie. Ubuntu).
2. Update your Ubuntu packages: `sudo apt update`
3. Once the packages have updated, install Redis with: `sudo apt install redis-server`
4. Confirm installation and get the version number: `redis-server --version`
5. To start running your Redis server: `sudo service redis-server start`

Check to see if redis is working (redis-cli is the command line interface utility to talk with Redis): `redis-cli ping` this should return a reply of "PONG".

To stop running your Redis server: sudo service redis-server stop