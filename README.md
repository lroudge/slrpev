# SlrpEV - data parsing from CSV files into MySQL database

## Table of contents
Files | Description
----- | -----------
interval.csv | csv file with fake data for the interval
session.csv | csv file with fake data for the session
models_csv.py | Python classes for Session and Interval, to be able to create an object and store it as a table row in the db
parse_csv.py | Python functions that parse the csv file, creates an object and stores it into the db as a row
dump.sql | Dump with the intervall (no it's not a typo) and session tables, populated with fake data

## Tutorial

### Install MYSQL
The first thing is going to be installing MySQL. For now, I think it's a good solution, but you might want to look into using another db later in the project.

If the Linux distribution is Ubuntu 14.04, here is how to install MySQL 5.7:
```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
```
Check the version:
```
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
```

While installing, it should ask you for a password for the root user. You need to type one in but make sure to take note of it somewhere, we're going to use it later.
If you're using another distrib or it didn't work, check out https://dev.mysql.com/doc/refman/8.0/en/linux-installation.html

In case you want to enter the MySQL server, do:
```
$ mysql -hlocalhost -uroot -p
Password: 
```
And enter the password you chose.

### Create the database in the MySQL server
After conecting inside the MySQL server, run:
```
mysql> CREATE DATABASE IF NOT EXISTS ecal_ev_charger;
```
Then you can grant specific permissions and create new users, but for now just using the root user is fine.

### Dump the tables in the db
To dump the fake data from the fake csv files and create the interval and session tables, run:
```
$ mysql -uroot -p < dump.sql
Password:
```
And enter your password. If you decided to use another user you can replace root by that user name.

### Install python3 and dependencies
This might also depend on the version of Linux you're using.
To install python3 on Ubuntu:
```
$ sudo apt-get update
$ sudo apt-get install python3.6
```
Otherwise, check out: https://docs.python-guide.org/starting/install3/linux/
Make sure pip3 is installed:
```
$ sudo apt install python3-pip
```

To install sqlalchemy:
```
pip3 install SQLAlchemy==1.2.5
```

### Run the script with the real csv files
The idea to make it smooth every time we get new csv files would be to replace the content of interval.csv and session.csv by the new files.

To do so, download those files on the server, in the same directory as the current csv files, and just do:
```
$ cat <whatever is the name of the csv for interval> > interval.csv
$ cat <whatever is the name of the csv for session> > session.csv
```

Now, you can simply run the script in the same directory like so:
```
$ ./parse_csv.py <mysql user name> <mysql password>
```

## Disclaimer
This is a rough draft that works, but feel free to modify the files in any way you like to fit the needs of the project.
