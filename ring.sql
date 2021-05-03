/* Let's rescue some torrents! */
USE unit3d;
SELECT id, category_id, featured, description
FROM unit3d.torrents WHERE seeders = 0;
