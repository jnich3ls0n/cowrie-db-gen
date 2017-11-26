# Custom Cowrie Database Generation Scripts

## Introduction
These scripts were an exercise in learning Python 3 SQL database interaction with SQLAlchemy and Pandas using collected
json data from a cowrie sensor.  SQLAlchemy is used to generate a sqlite3 database and to populate the database with
cowrie events and ip location data from the GeoLite2 City database.  The database is queried using Pandas and the event
data is displayed in a Jupyter Notebook. 

## Requirements
* Ubuntu 16.4
* Python 3
* SQLAlechemy
* Pandas
* GeoIP2
* Jupyter Notebook
* Latest GeoLite2 City Database
* Remote Cowrie Sensor

## Install and Configure
See INSTALL.md

## Running the Scripts
1. `cd cowrie_db_gen/` 
2. Run `./get_logs.sh` to populate the json/ directory with the cowrie json logs
3. Run `python3 declarative.py` to create a new sqlite3 database in the db/ dir
4. Run `python3 populate_db.py` to populate the database with cowrie event and ip-location data.
5. Run `jupyter notebook ip_location_display.ipynb` to open the Jupyter Notebook
6. Select Kernel -> Restart &amp; Run All to display the collected data
