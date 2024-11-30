# imgscraper

CLI tool for downloading all the image files from a particular URL.

## Setup

`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

## Usage

```
usage: imgscraper [-h] [--headless] url dir

Use selenium to download all images on a particular webpage to a single
directory.

positional arguments:
  url         URL to download images from
  dir         Path to the directory in which to save the images

options:
  -h, --help  show this help message and exit
  --headless  run without visually opening a browser window
```

## Example

`python -m imgscraper --headless https://www.python.org ./python_images`
