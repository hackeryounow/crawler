### Overview
The Crawler is to scrape plmns from the website of the Global Mobile Platform. [link](https://www.mcc-mnc.com/)

### How to use
1. Create Database and a table to store the data
   ```sql
   -- 1. create database
   CREATE DATABASE IF NOT EXISTS slicenet;
   
   -- 2. use database
   USE slicenet;
   
   -- 3. create table
   CREATE TABLE plmns (
       MCC VARCHAR(3) NOT NULL,
       MNC VARCHAR(3) NOT NULL,
       ISO VARCHAR(10),
       Country VARCHAR(100),
       Country_Code VARCHAR(10),
       Network VARCHAR(100),
       PRIMARY KEY (MCC, MNC, Country_Code, Network)
   );
   
   -- 4. insert a data into the table for test
   INSERT INTO plmns (MCC, MNC, ISO, Country, Country_Code, Network) VALUES 
   ('310', '260', 'USA', 'United States', '1', 'T-Mobile');
   -- 5. truncate the table
   truncate table plmns;
   ```
2. Configure the database connection in `settings.py`
   - `driver`: the driver of the database
   - `host`: the host of the database
   - `port`: the port of the database
   - `user`: the user of the database
   - `password`: the password of the database
   - `db`: the name of the database
   - `auth_plugin`: the authentication plugin of the database
    ```
    MYSQL_DB_CONFIG = {
        "driver": "mysql.connector",
        "host": "******",
        "port": 3306,
        "user": "hacku",
        "password": "******",
        "db": "slicenet",
        "auth_plugin": "mysql_native_password"
    }
    ```
2. Run `python ./mobileplmn/start.py`
