# Image Resizer

Image Resizer script allows you to, surprise, resize images.

# Requirements

Pillow library must be intalled, so input either

```bash
pip install Pillow
```

or

```bash
pip install -r requirements.txt
```

# Usage

Image Resizer 

Required parameters:

- Path to file to resize

Optional parameters:

- `--width`: desired width
- `--heigth`: desired height
- `--scale`: desired scale. Scale can't be used with width or height
- path to directory where the result should be saved

Example:

```bash
$ python image_resize.py cat.png ~/Downloads/ --width 200 --height 300 
```

```bash
$ python image_resize.py cat.png --width 200 --height 300 
```

```bash
$ python image_resize.py cat.png --scale 1.5 
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
