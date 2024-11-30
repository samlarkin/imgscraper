"""File operations for imgscraper"""

import os
import sys
import subprocess
from pathlib import Path


def get_output_path(dirname):
    """Get output path Path object"""
    if dirname == '.':
        return  Path.cwd()
    return Path(dirname)


def make_output_dir(path):
    """Make output directory if it doesn't exist"""
    os.makedirs(path, exist_ok=True)


def get_file_ext(path):
    """Get appropriate file extension with system file --ext command"""
    command = ['file', '--ext', path]
    try:
        text = subprocess.check_output(command).decode('utf-8')
        ext = text.strip().split(': ')[1].split('/')[0]
        return ext

    except OSError:
        print >> sys.stderr, 'Could not check file type with file --ext'


def add_extensions(path):
    """Add file extensions to all files in path"""
    for file in path.iterdir():
        ext = get_file_ext(file)
        if ext is None:
            continue
        os.rename(file, path/f'{file.name}.{ext}')
