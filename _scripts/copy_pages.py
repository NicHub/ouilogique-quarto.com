"""

"""

import logging
import os
import shutil

pwd = os.path.abspath(os.curdir)
prefix = "../" if "_scripts" in pwd else "./"
SOURCE_PATH = f"{prefix}pages/"
DEST_PATH = f"{prefix}_site/"


def main():
    """___"""
    if not os.path.exists(SOURCE_PATH):
        raise SystemExit(f"{__file__} => {SOURCE_PATH} not found")

    for dir in os.listdir(SOURCE_PATH):
        if dir in [".DS_Store"]:
            continue
        source_path = f"{SOURCE_PATH}{dir}"
        dest_path = f"{DEST_PATH}{os.path.split(dir)[1]}"
        print(source_path)
        print(dest_path)
        print()
        shutil.copytree(source_path, dest_path, dirs_exist_ok=True)


try:
    logging.basicConfig(
        format="%(levelno)s " "%(module)-11s " "%(lineno)3s. " "%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    main()
except SystemExit as _e:
    logging.error(_e)
else:
    logging.info("DONE")
