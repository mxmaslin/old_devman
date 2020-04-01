# Shop Score Page

## Project features

The app allows to track orders statuses by fetching the updates on them every 10 seconds from database.

The orders' statuses are following:

- green: order's processing wait time is less than 7 minutes.
- yellow: order's processing wait time is less than 30 minutes.
- red: order's processing wait time is more than 30 minutes.

The app also outputs the following secondary information:

- amount of unprocessed orders.
- amount of orders processed during the current day.

Web-interface of the app can be accessed at [https://mx-score.herokuapp.com](https://mx-score.herokuapp.com).   

## Local deploy

1. Install requirements `pip install -r requirements.txt`
2. Run `flask run`
3. Open http://127.0.0.1:5000 in browser window.

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
