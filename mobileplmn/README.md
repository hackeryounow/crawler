### Overview
The Crawler is to scrape plmns from the website of the Global Mobile Platform. [link](https://www.mcc-mnc.com/)

### How to use
1. Configure the database connection in `settings.py`
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
