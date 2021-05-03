#!/opt/homebrew/bin/python3
# Testing stuff
import yaml
import os

# Dynamically load in our magic config files
configname = os.path.expanduser('~/.rcc-tools.yml')
config = yaml.safe_load(open(configname))

# Check if the config is empty
if config is None:
    print("Failed to load configuration.")
    sys.exit(1338)

# Set our mysql password
qbtpass = config["qbtpassword"]

from qbittorrent import Client

qb = Client('http://127.0.0.1:8080/')

qb.login('admin', qbtpass)
# not required when 'Bypass from localhost' setting is active.
# defaults to admin:admin.
# to use defaults, just do qb.login()

torrents = qb.torrents()

for torrent in torrents:
    print(torrent['name'])
