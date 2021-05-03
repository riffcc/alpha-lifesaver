#!/opt/homebrew/bin/python3
# Script to throw a lifesaver at dead Riff.CC releases! :)

# Uses homebrew py3 because I am a bad person
# Credits:
#  - https://stackoverflow.com/questions/10195139/how-to-retrieve-sql-result-column-value-using-column-name-in-python
#  - https://github.com/PyMySQL/PyMySQL

# Import needed modules
from __future__ import with_statement
from grizzled.os import working_directory
import os, sys, yaml, re

# Setup URL parser, thanks https://www.geeksforgeeks.org/python-check-url-string/
def ParseFindURLs(string):
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]

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
            print("Processing id "+ str(id))
            description = row["description"]
            # Grab our source from the description. Hopefully.
            # Set up some empty arrays
            urlLines = []
            actualURLs = []
            for line in description.splitlines():
                if "Source: [url]" in line:
                    print(line)
                    urlLines.append(line)
            for line in urlLines:
                # Sanitize the line
                line = line.replace('[url]', '')
                line = line.replace('[/url]', '')
                actualURLs.append(ParseFindURLs(line))

            # Go grab that source based on rules
            for actualURL in actualURLs:
                for lololol in actualURL:
                    print(lololol)

            # Fetch the torrent
            #go("https://u.riff.cc/torrents/download/" + str(id))
            #with working_directory("/tmp/torrents/"):
                #save_html(str(id) + ".torrent")
