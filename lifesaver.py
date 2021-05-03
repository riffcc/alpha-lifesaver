#!/opt/homebrew/bin/python3
# Uses homebrew py3 because I am a bad person
# https://stackoverflow.com/questions/10195139/how-to-retrieve-sql-result-column-value-using-column-name-in-python
# https://github.com/PyMySQL/PyMySQL

# Script to throw a lifesaver at Riff! :)
import mysql.connector
import os
import yaml

# Dynamically load in our magic config files
configname = os.path.expanduser('~/.rcc-tools.yml')
config = yaml.safe_load(open(configname))

# Check if the config is empty
if config is None:
    print("Failed to load configuration.")
    sys.exit(1338)

# Set our mysql password
password = config["password"]

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='unit3d',
                             password=password,
                             database='unit3d',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `description` FROM `torrents`"
        cursor.execute(sql)
        result_set = cursor.fetchall()
        for row in result_set:
            print("%s, %s" % (row["id"], row["description"]))
