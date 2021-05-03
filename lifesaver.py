#!/opt/homebrew/bin/python3
# Uses homebrew py3 because I am a bad person

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

mydb = mysql.connector.connect(
  host="localhost",
  user="unit3d",
  password=password,
  database="unit3d"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM torrents")

myresult = mycursor.fetchall()

row = dict(zip(mycursor.column_names, mycursor.fetchone()))
print("{description}".format(row))

cursor = cnx.cursor()
cursor.execute(...)
row = dict(zip(cursor.column_names, cursor.fetchone()))
