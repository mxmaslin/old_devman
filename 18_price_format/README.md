# Price Formatter

Price formatter script modifies representation of numbers like `1234` to `1 234.00` format.

# Usage

```bash
$ format_price.py 1234
1 234.00
```

Price formatter functionality can be used outside of format_price.py. To use it other program, import `format_price` function.

```python
>>> from format_price import format_price
>>> print(format_price(1234))
1 234.00
``` 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
