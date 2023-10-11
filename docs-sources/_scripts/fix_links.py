"""

Fix wrong link in `all.css`.

The bug comes from the function
`quarto.doc.add_html_dependency`
called by `fontawesome.lua`.

"""

import os
import logging
import yaml

pwd = os.path.abspath(os.curdir)
prefix = "../" if "_scripts" in pwd else "./"

with open(f"{prefix}_quarto.yml", "rt") as _f:
    quarto_yaml = yaml.safe_load(_f.read())


FPATH = f'{prefix}{quarto_yaml["project"]["output-dir"]}/site_libs/quarto-contrib/fontawesome6-0.1.0/all.css'


STR1 = "../../webfonts"
STR2 = "1e21o67"


def main():
    """___"""
    if not os.path.exists(FPATH):
        raise SystemExit(f"{__file__} => {FPATH} not found")

    with open(FPATH, "rt", encoding="utf-8") as _f:
        content = _f.read()
        if STR2 not in content:
            raise SystemExit(f"{__file__} => {STR2} not found in {FPATH}")
        content = content.replace(STR1, STR2)

    with open(FPATH, "wt", encoding="utf-8") as _f:
        _f.write(content)


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
