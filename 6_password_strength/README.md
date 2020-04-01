# Password Strength Calculator

## Description

`password_strength.py` script determines a strength of you password by grading it from 1 to 10.

To ensure password strength, it is being checked whether it is present in blacklist. You can download blacklist at [https://github.com/danielmiessler/SecLists/tree/master/Passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

Password strength rating:

- 1: password is in the blacklist or has length of 1
- +3 points for each passed check:
    - password passes check of length (must be greater of equal 6)
    - presence of
        - mixed case letters
        - both letters and digits
        - special characters
- 10 if password has passed all checks 

# Using script

## Input

```bash
$ python password_strength.py <path to blacklist>
Please enter password:
```

## Output

```bash
Password strength: 10
```

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
