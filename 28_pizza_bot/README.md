# Telegram Bot for Pizzeria

The telegram bot outputs pizzeria's menu to chat and automates order calculation.
Also there is admin section to create a new pizzas.

# How to Use

Step 0. Install requirements

    pip install -r requirements.txt

Step 1. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

Step 2. Start bot

```
#!bash

$ # the token below is not actual, you need to register a new one
$ BOT_TOKEN="110831855:AAE_GbIeVAUwk11O12vq4UeMnl20iADUtM" python3 bot.py
```

Step 3. Upload initial pizzas data

    python upload_data_to_db.py
    
Step 4. Run application

    flask run

Please note that first login won't lead you to <ADDRESS:PORT>/admin. It's known
 issue (https://github.com/mattupstate/flask-security/issues/263). 

- Login: [127.0.0.1:5000/login](127.0.0.1:5000/login])
- Logout: [127.0.0.1:5000/logout](127.0.0.1:5000/logout)
- Admin: [127.0.0.1:5000/admin](127.0.0.1:5000/admin)


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

