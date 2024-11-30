"""Main procedure for imgscraper"""

import requests
from pathlib import Path

from .cli import cli
from .file import get_output_path, make_output_dir, add_extensions
from .scraper import ImgScraper


def main():
    """Download all images from url to directory"""
    args = cli()
    output_path = get_output_path(args.dir)
    make_output_dir(output_path)
    scraper = ImgScraper(args.url, output_path, headless=args.headless)
    scraper.download_images()
    add_extensions(output_path)


if __name__ == '__main__':
    main()
