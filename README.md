# Pur Beurre

Pure Beurre is a Python application made with the Django framework. This allows the user to search for a substitute food based on nutrition grade.

## Start guide

### Dependencies

* [Python 3.6 or more](https://www.python.org) is required
* [PostGreSQL](https://www.postgresql.org/download/)

### Installation instructions

* install Python 3.6 or more
* install PostgreSQL

Create a database and a proprietary user account for this database.

Ubuntu example:

    $ sudo -i -u postgres
    $ createuser -P --interactive <user_name>
    Enter password for new role:
    Enter if again:
    Shall the new role be a superuser? (y/n) n
    Shall the new role be allowed to create databases? (y/n) y
    Shall the new role be allowed to create more new roles? (y/n) y
    $ createdb -O <user_name> -E UTF8 <database_name>

Collect the pur_beurre repo and install the dependencis as below:

    $ git clone https://github.com/Nels885/pur_beurre.git
    $ cd pur_beurre
    $ pip3 install -r requirements.txt
    

    
