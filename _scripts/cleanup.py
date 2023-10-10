"""


"""

import os
import logging
import yaml


pwd = os.path.abspath(os.curdir)
prefix = "../" if "_scripts" in pwd else "./"
with open(f"{prefix}_quarto.yml", "rt") as _f:
    quarto_yaml = yaml.safe_load(_f.read())


PATHS = [
    f'{os.path.abspath(os.curdir)}{os.path.sep}..{os.path.sep}{quarto_yaml["project"]["output-dir"]}'
]
print(PATHS)
print(quarto_yaml["project"]["output-dir"])


def main():
    """___"""
    for path in PATHS:
        print(path)
        if os.path.exists(path):
            os.removedirs(path)
            logging.info(f"{path} deleted")
        else:
            logging.info(f"{path} not found")


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
