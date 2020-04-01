# Sites Monitoring Utility

Sites monitoring script reads urls from file and checks whether

- server responds with HTTP 200
- domain name paid for more than `N` days where `N` is amount of days

# Usage

Prior to use, install the dependencies:

```bash
pip install -r requirements.txt
```

Example of usage:

```bash
$ python check_sites.py 30 
http://d3.ru responded with HTTP 200. Expriration date is less than 30 day(s).
http://yandex.ru responded with HTTP 200. Expriration date is more than 30 day(s).
asdf does not exist.
http://pornhub.com responded with HTTP 200. Expriration date is more than 30 day(s).
``` 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
