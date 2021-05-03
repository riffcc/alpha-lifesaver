#!/opt/homebrew/bin/python3
# Script to throw a lifesaver at Riff! :)
# Uses homebrew py3 because I am a bad person
# Credits:
#  - https://stackoverflow.com/questions/10195139/how-to-retrieve-sql-result-column-value-using-column-name-in-python
#  - https://github.com/PyMySQL/PyMySQL
# Import needed modules
from __future__ import with_statement
from grizzled.os import working_directory
import os
import sys
import yaml

# Set our API key
from pathlib import Path
apiname = os.path.expanduser('~/.rcc-api')
apitoken = Path(apiname).read_text()

# Dynamically load in our magic config files
configname = os.path.expanduser('~/.rcc-tools.yml')
config = yaml.safe_load(open(configname))

# Check if the config is empty
if config is None:
    print("Failed to load configuration.")
    sys.exit(1338)

# Get our Riff.CC credentials and load them in
rccuser = config["rccuser"]
rccpass = config["rccpass"]
sqlpassword = config["password"]

# Login to Riff.CC
# https://stackoverflow.com/questions/2910221/how-can-i-login-to-a-website-with-python

from twill.commands import *
go('https://u.riff.cc/login')

showforms()
fv("1", "username", rccuser)
fv("1", "password", rccpass)

submit('0')

# Set our mysql password

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='unit3d',
                             password=sqlpassword,
                             database='unit3d',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `description` FROM `torrents` WHERE seeders = 0"
        cursor.execute(sql)
        result_set = cursor.fetchall()
        for row in result_set:
            id = row["id"]
            print("id is: " + str(id))
            row["description"]
            description = (row["description"][:120] + '...') if len(row["description"]) > 120 else row["description"]
            print("Description is: \n" + description)
            # Fetch the torrent
            go("https://u.riff.cc/torrents/download/" + str(id))
            with working_directory("/tmp/torrents/"):
                save_html(str(id) + ".torrent")
