"""


"""

import os
import logging
import yaml
import fnmatch

logging.basicConfig(
    format="%(levelno)s " "%(module)-11s " "%(lineno)3s. " "%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

QUARTO_YML_FNAME = "_quarto.yml"
while True:
    if os.path.isfile(QUARTO_YML_FNAME):
        logging.info(f"{QUARTO_YML_FNAME} found")
        break
    else:
        pwd = os.path.abspath(os.curdir)
        if pwd == os.path.abspath(os.sep):
            raise SystemExit(f"{QUARTO_YML_FNAME} not found. Abort.")
        os.chdir("..")

with open(QUARTO_YML_FNAME, "rt", encoding="utf-8") as _f:
    QUARTO_YML = yaml.safe_load(_f.read())

try:
    PROJECT_RENDERS = QUARTO_YML["project"]["render"]
except KeyError:
    raise SystemExit(f'{QUARTO_YML_FNAME} has no ["project"]["render"] keys.')


def search_file(dir, fname):
    chemins_fichiers_trouves = []
    for dossier, _, fichiers in os.walk(dir):
        for fichier in fichiers:
            if fnmatch.fnmatch(fichier, fname):
                chemin_fichier = os.path.join(dossier, fichier)
                chemins_fichiers_trouves.append(chemin_fichier)
    return chemins_fichiers_trouves


for project_render in PROJECT_RENDERS:
    if project_render == "./index.qmd":
        continue
    if os.path.isdir(project_render):
        FILES = search_file(project_render, "index.qmd")


def readyaml_header(file_path):
    """___"""
    yaml_header = ""
    content = ""
    cnt = 0
    with open(file_path, "rt", encoding="utf-8") as _f:
        for line in _f:
            if line[:3] == "---":
                cnt += 1
                continue
            if cnt < 2:
                yaml_header += line
            else:
                content += line
    yaml_header = yaml.safe_load(yaml_header)
    return yaml_header, content


FILES_NO_DRAFT = []
for file in FILES:
    yaml_header, _ = readyaml_header(file)
    try:
        if not yaml_header["draft"]:
            file = file.replace("index.qmd", "")
            if file[:2] == "./":
                file = file[1:]
            FILES_NO_DRAFT.append(file)
    except KeyError:
        pass


fpath = "./js/file_list.js"
with open(fpath, "wt", encoding="utf-8") as _f:
    _f.write("file_list = {\n")
    for id, file in enumerate(sorted(FILES_NO_DRAFT, reverse=True)):
        _f.write(f'"{file}": {id},\n')
    _f.write("}\n")

try:
    pass
except SystemExit as _e:
    logging.error(_e)
    # logging.error(f"BASE_PATH = {BASE_PATH}")
    # logging.error(f"DEST_PATH_POSTS = {DEST_PATH_POSTS}")
    # logging.error(f"FILES = {FILES}")
else:
    logging.info("DONE")
