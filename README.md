
### Setting up MySQL

- sudo apt-get update
- sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
- pip install PyMySQL
- sudo mysql_secure_installation
- mysql -u root -p
- create database myproject character set utf8;
- create user myprojectuser@localhost identified by 'Password@0';
- grant all privileges on myproject.* to myprojectuser@localhost;
- flush privileges;
- exit


### Setting up Django

- sudo pip install virtualenv
- virtualenv myvenv
- source myvenv/bin/activate
- pip install django mysqlclient

### Running the project

- cd ~/Airport_Management-System/airport
- Add these two lines in __init__.py: 
<br> import pymysql 
<br> pymysql.install_as_MySQLdb()
- python manage.py makemigrations
- python manage.py sqlmigrate flights 0001
- python manage.py migrate
- python manage.py runserver


