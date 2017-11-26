# Installation Instructions

## Configure a Remote Cowrie Sensor
Cowrie Project: https://github.com/micheloosterhof/cowrie

## Clone this Project


## Download the latest GeoLite2 City Database
1. Download the latest GeoLite2 City database here: https://dev.maxmind.com/geoip/geoip2/geolite2/
2. Save the database to db/

## Install Jupyter Notebook
I highly recommend downloading Anaconda v3.x from Continuum Analytics which comes packaged with Juypter Notebook,
SQLAlchemy, and Pandas: https://www.anaconda.com/download/ 

## Install Python 3 Dependencies
1. `cd cowrie_db_gen.py/`
2. `pip install -r requirements.txt` or `pip3 install -r requirements.txt` depending on your configuration

## Configure the Script Settings

### get_logs.sh
- `SENSOR_USER="{valid username on the sensor}"`
- `SENSOR_IP="{ip address of the sensor}"`
- `SENSOR_PORT={SSH Port}`
- `SENSOR_LOG_DIR="{cowrie log directory on the sensor (probably /home/cowrie/cowrie/log/)}"`

### declarative.py
- `DB_NAME = "{database name (default='sqlite3.db')}"`

### populate_db.py
- `LOCATION_DB = "{GeoLite2 City database name (default='GeoLite2-City.mmdb')}"`
