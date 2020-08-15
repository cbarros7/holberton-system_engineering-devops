#!/usr/bin/env bash
# task advance with pupppet
exec { 'http header':
    command  => 'sudo apt-get update -y;
	sudo apt-get install nginx -y;
	sudo sed -i "/servername /a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
	sudo service nginx restart',
    provider => shell,
}
