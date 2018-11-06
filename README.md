# Airport Management System 
Course project for Database Management System CO301

## Install components
```bash
sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
sudo apt-get install wkhtmltopdf
```

### Setting up MySQL 
```bash
sudo mysql_secure_installation
mysql -u root -p
create database airportdb character set utf8;
create user airportuser@localhost identified by 'Password@0';
grant all privileges on airportdb.* to airportuser@localhost;
flush privileges;
exit
```

### Setting up Virtual Environment and Install Requirements
```bash
sudo pip install virtualenv
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

### Running the project
```bash
cd ~/Airport_Management-System
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


