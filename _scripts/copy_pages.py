"""

"""

import logging
import os
import shutil

SOURCE_PATH = "./pages"
DEST_PATH = "./_site/"


def main():
    """___"""
    if not os.path.exists(SOURCE_PATH):
        raise SystemExit(f"{__file__} => {SOURCE_PATH} not found")
    if not os.path.exists(DEST_PATH):
        raise SystemExit(f"{__file__} => {SOURCE_PATH} not found")

    for dir in SOURCE_PATH:
        dest_path = f"{DEST_PATH}{os.path.split(dir)[1]}"
        shutil.copytree(dir, dest_path, dirs_exist_ok=True)


try:
    logging.basicConfig(
        format="%(levelno)s " "%(module)-11s " "%(lineno)3s. " "%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )
    main()
except SystemExit as _e:
    logging.error(_e)
else:
    logging.info("DONE")
