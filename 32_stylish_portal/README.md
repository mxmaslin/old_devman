# Shared CSS Library

`nginx.conf` file contains configuration for two sites. The configuration substitutes css styles file.

# How to Test

Install nginx. On macos, it will be

    brew install nginx
    
Run nginx

    sudo nginx

Make symlink

    sudo ln -sf $(pwd)/nginx.conf /usr/local/etc/nginx/nginx.conf

Restart nginx

    sudo nginx -s reload
    
Check

    http://127.0.0.1:8080
    http://127.0.0.1:8081

Запуск uwsgi: 

    uwsgi socket first.sock --module first.wsgi --chmod-socket=664 
   
In case of nginx errors, refer to

    tail /usr/local/var/log/nginx/error.log 

    /usr/local/etc/nginx/nginx.conf
    
    nginx -t

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
