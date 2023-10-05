import os
import shutil
from pprint import pprint

import yaml

SOURCE_PATH = os.path.expanduser("~/Sites/ouilogique.com/")
SOURCE_PATH_POSTS = os.path.expanduser("~/Sites/ouilogique.com/_posts/blog/")
DEST_PATH = "../"
DEST_PATH_POSTS = "../posts/"
FILES = os.listdir(SOURCE_PATH_POSTS)


def trouver_doublons(liste):
    dictionnaire = {}
    doublons = []

    for element in liste:
        if element in dictionnaire:
            if dictionnaire[element] == 1:
                doublons.append(element)
            dictionnaire[element] += 1
        else:
            dictionnaire[element] = 1

    return doublons


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
    # print(yaml_header)
    # print(content)

    return yaml_header, content


UNIQUE_TAGS = []


def list_tags(fpath):
    """___"""
    yaml_header, _ = readyaml_header(fpath)
    yaml_header = yaml.safe_load(yaml_header)
    if yaml_header["tags"]:
        # print(fpath)
        # print(yaml_header["tags"])
        for tag in yaml_header["tags"]:
            if tag not in UNIQUE_TAGS:
                UNIQUE_TAGS.append(tag)


IMAGE_FEATURES = []


def list_image_feature(fpath):
    """___"""
    yaml_header, _ = readyaml_header(fpath)
    yaml_header = yaml.safe_load(yaml_header)
    if yaml_header["image"]["feature"]:
        IMAGE_FEATURES.append(yaml_header["image"]["feature"])


def normalize_image_feature(fpath, fname):
    """___"""
    yaml_header, _ = readyaml_header(fpath)
    yaml_header = yaml.safe_load(yaml_header)
    has_feature = True if yaml_header["image"]["feature"] else False
    if has_feature:
        content = ""
        with open(fpath, "rt", encoding="utf-8") as _f:
            content = _f.read()
        old_name = yaml_header["image"]["feature"]
        separator = old_name.split(".")[-1]
        new_name = f"banner_{fname[:-2]}{separator}"
        print(old_name)
        print(new_name)
        content = content.replace(old_name, new_name)
        with open(fpath, "wt", encoding="utf-8") as _f:
            _f.write(content)
        base_path = os.path.expanduser("~/Sites/ouilogique.com/images/")
        imgpath1 = f"{base_path}{old_name}"
        imgpath2 = f"{base_path}{new_name}"
        print(imgpath1)
        print(imgpath2)
        # raise SystemExit
        shutil.copyfile(imgpath1, imgpath2)
        os.remove(imgpath1)
    return has_feature


def main():
    for fname in FILES:
        fpath = f"{SOURCE_PATH_POSTS}{fname}"
        list_tags(fpath)
        list_image_feature(fpath)
    # pprint(UNIQUE_TAGS)
    pprint(IMAGE_FEATURES)

    doublons = trouver_doublons(IMAGE_FEATURES)
    print(doublons)
    # raise SystemExit

    for fname in FILES:
        fpath = f"{SOURCE_PATH_POSTS}{fname}"
        has_feature = normalize_image_feature(fpath, fname)
        # if has_feature:
        #     raise SystemExit


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        print("Early Exit!")
