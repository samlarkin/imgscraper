"""A simple cli for imgscraper"""

import argparse


def cli():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        prog='imgscraper',
        description='Use selenium to download all images on a particular ' \
        'webpage to a single directory.'
    )
    parser.add_argument(
        'url',
        help='URL to download images from'
    )
    parser.add_argument(
        'dir',
        help='Path to the directory in which to save the images'
    )
    parser.add_argument(
        '--headless',
        action='store_true',
        help='run without visually opening a browser window'
    )
    return parser.parse_args()
