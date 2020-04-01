# Timer for Websites That Steal Your Time

This project helps to control time was spent on sites. It requires special extension for Chrome browser.

# Installing

Install extension for Chrome browser [Custom JavaScript for websites](https://chrome.google.com/webstore/detail/custom-javascript-for-web/poakhlngfciodnhlhhgnaaelnpjljija).

Open configuration of [cjs](https://chrome.google.com/webstore/detail/custom-javascript-for-web/poakhlngfciodnhlhhgnaaelnpjljija) browser extension on the site you want to control. Unfortunately, at the moment of writing this, "your own external scripts" cjs feature is not working, so you need to get your hands dirty and copy the [contents of index.js](https://github.com/mxmaslin/34_timemachine/blob/master/index.js) to cjs's text area input. Don`t forget to press "enable cjs for this host" to enable custom JS.

When the timer is activated, it starts 3-minute countdown, and then diplays an alert containing one of the witty quotes aiming to prevent you from procrastination. This alert will pop up every 30 seconds.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
