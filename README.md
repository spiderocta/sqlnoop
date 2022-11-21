<p align="center">
  <img src="https://github.com/spiderocta/sqlNoop/blob/master/images/icon.ico" height="120">
  <h2 align="center">SQLNoop</h2>
</p>

<p align="center">
  <a href="#about" title="About">About</a> |
  <a href="#installing" title="Installing">Installing</a> |
  <a href="#screenshots" title="Screenshots">Screenshots</a> |
  <a href="#usage" title="Usage">Usage</a> |
  <a href="#database-support" title="Database Support">Database Support</a> |
  <a href="#features" title="Features">Features and Compatibility</a> |
  <a href="#releases" title="Releases">Releases</a> |
  <a href="#contributing" title="Contributing">Contributing</a>
</p>

<br>

## Status 

![100%](https://progress-bar.dev/100/?title=Done)
<br /> 

## About
`SQLNOOP` is a simple graphical user interface to interact with MySQL Database.

`SQLNOOP` provides a simple way to define the schema in  MySQL Database via a graphical user interface.

`SQLNOOP` supports testing connection with a server + baisc and core `SQL` operations, such as [creating and selecting databases](https://dev.mysql.com/doc/refman/8.0/en/creating-database.html),
[create tables](https://dev.mysql.com/doc/refman/8.0/en/create-table.html), 
[alter tables](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html), and other useful statement like [show databases](https://dev.mysql.com/doc/refman/8.0/en/show-databases.html)
and has additional feature that many apps don't have, which is `bad design` and [less database support][Database Support].


## Installing 
this is a one-file python program `easy to use and run` first you need to have python3 installed on your system after cloning the repo you can easily run the command
`python sqlNoop.py` if you have more than one version use `pythonX sqlNoop.py` where x is the version .or you can just double click the `sqlNoop.py` file if on windows and it will show up. 

***note : Required modules before running the code :*** 

- tkinter
- pymysql-1.0.2 

``` 
pip install tkinter 
``` 
after executing this you may encounter the below error : 
```
ERROR: Could not find a version that satisfies the requirement tkinter (from versions: none)
ERROR: No matching distribution found for tkinter
``` 

to resolve this you have to use `apt-get install python3-tk` instead. 

second to install pymysql you need to run `pip install pymysql`

***note : for those who faces _tkinter.TclError: bitmap on linux just head to  [#1](/../../issues/1) to solve it :*** 

## Screenshots 

![app image](https://github.com/spiderocta/sqlNoop/blob/master/app_image1.png)
![app image](https://github.com/spiderocta/sqlNoop/blob/master/app_image.png)

## Usage
as shown on the image above each button or component says what it does : 
| Component                      | Description                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------|
| `show databases`               | internaly executes `SHOW DATABASES`                                                  |
| `createDB`                     | internaly executes `CREATE DATABASE` with the name from the field                    |
| `create table`                 | shows the `Table Column` Frame asking for table with only one column details         |
| `create table with column`     | internaly executes ` CREATE TABLE <NAME> (<COL_NAME> <TYPE>(<LENGTH>)`               |
| `add columns`                  | shows the `new Columns` Frame asking for more columns details                        |
| `add new columns`              | internaly executes `ALTER TABLE <TABLE NAME> ADD COLUMN <COL_NAME> <TYPE>(<LENGTH>)` |
| `server name`                  | local or remote server address to connect to                                         |
| `username`                     | username for the server or the database                                              |
| `password`                     | password for the server or the database                                              |
| `connect`                      | this button will establish the connection using the given details in the fields      |



## Database Support 
`SQLNOOP` works with `MySQL`, `ORACLE`, `PosgreSql` and many of the relational ones as it only deals with simple DDL and common statements.

## Features
The `SQLNOOP` project's goal is to support all DDL haters,  you can use it to create tables and columns easily without writing the command yourself.
and start hacking the planet with the actual code.

## Releases 
[v1.0-Beta](https://github.com/spiderocta/sqlNoop/releases/tag/v1.0-beta)


## Contributing
In case you find a bug or have a suggested improvement, [The issue tracker](https://github.com/spiderocta/sqlNoop/issues) is the preferred channel for bug reports, features requests and submitting pull requests.

### what to do 
* Fork it!
* Create your feature branch: git checkout -b my-new-feature
* Commit your changes: git commit -am 'Add some feature'
* Push to the branch: git push origin my-new-feature
* Submit a pull request



