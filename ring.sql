/* Let's rescue some torrents! */
USE unit3d;
SELECT id, category_id, featured, description
FROM `torrents` WHERE seeders = 0
INTO OUTFILE '/var/lib/mysql-files/ring.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n';
