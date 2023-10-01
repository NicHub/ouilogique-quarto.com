"""

"""
import os
import shutil
from pprint import pprint

import markdown_link_extractor
import yaml


def copy_posts_from_jekyll_to_qarto(source_file, dest_dir, dest_file):
    """___"""
    os.makedirs(f"{dest_dir}", exist_ok=True)
    shutil.copyfile(source_file, dest_file)


def make_yaml_header_compliant(fpath):
    """___"""
    with open(fpath, "rt", encoding="utf-8") as _f:
        content = (
            _f.read()
            .replace("comments:", "comments_:")
            .replace("    feature:", "image:")
            .replace("image:\n", 'image: ""\n')
        )
    content = content.replace('image: ""\nimage: ', "image: ")
    content = content.replace('image: ""\n', "")
    with open(fpath, "wt", encoding="utf-8") as _f:
        _f.write(content)


def extract_img_links_and_copy_img(dest_dir, dest_file):
    """___"""
    with open(dest_file, "rt", encoding="utf-8") as _f:
        content = _f.read()
    links = markdown_link_extractor.getlinks(content)

    # pprint(links)

    global COUNT_LINKS
    for link in links:
        if (
            ".tif" in link.lower()
            or ".jpg" in link.lower()
            or ".jpeg" in link.lower()
            or ".png" in link.lower()
            or ".svg" in link.lower()
        ):
            if "../../" in link:
                COUNT_LINKS += 1
                img_name = os.path.split(link)[-1]
                img_name = os.path.split(link)[-1]
                content = content.replace(link, f"./images/{img_name}")
                source_img_path = link.replace(
                    "../../", os.path.expanduser("~/Sites/ouilogique.com/")
                )
                dest_dir_img = f"{dest_dir}images/"
                os.makedirs(f"{dest_dir_img}", exist_ok=True)
                dest_img_path = f"{dest_dir_img}{img_name}"
                if not os.path.exists(source_img_path):
                    raise SystemExit(f"{source_img_path} not found")
                shutil.copyfile(source_img_path, dest_img_path)

    with open(dest_file, "wt", encoding="utf-8") as _f:
        _f.write(content)

    return links


def extract_feature_img_links_and_copy_img(dest_dir, dest_file):
    """___"""

    yaml_header = ""
    cnt = 0
    with open(dest_file, "rt", encoding="utf-8") as _f:
        for line in _f:
            if cnt == 2:
                break
            if line[:3] == "---":
                cnt += 1
                continue
            yaml_header += line

    img_feature = None
    feature_img_path = None
    try:
        yaml_header = yaml.safe_load(yaml_header)
        img_feature = yaml_header["image"]
        if img_feature is None or len(img_feature) == 0:
            raise KeyError(
                f"Le champ `image_/feature` n’existe pas dans le fichier YAML."
            )
        feature_img_dir = os.path.expanduser("~/Sites/ouilogique.com/_site/images/")
        feature_img_path = f"{feature_img_dir}{img_feature}"
        if not os.path.exists(feature_img_path):
            raise SystemExit(f"{feature_img_path} not found")
    except KeyError:
        pass
    except TypeError:
        pass
    except:
        pass
    else:
        dest_img_dir = f"{dest_dir}images/"
        os.makedirs(dest_img_dir, exist_ok=True)
        dest_img_path = f"{dest_img_dir}/{img_feature}"
        # pprint(f"img_feature = {img_feature}")
        shutil.copyfile(feature_img_path, dest_img_path)
        with open(dest_file, "rt", encoding="utf-8") as _f:
            content = _f.read().replace(img_feature, f"./images/{img_feature}")
        with open(dest_file, "wt", encoding="utf-8") as _f:
            _f.write(content)


def main():
    """___"""
    for file in FILES:
        dirname = file.split(".")[0]
        source_file = f"{SOURCE_PATH}{file}"
        dest_dir = f"{DEST_PATH}{dirname}/"
        dest_file = f"{dest_dir}index.qmd"
        copy_posts_from_jekyll_to_qarto(source_file, dest_dir, dest_file)
        make_yaml_header_compliant(dest_file)
        extract_img_links_and_copy_img(dest_dir, dest_file)
        extract_feature_img_links_and_copy_img(dest_dir, dest_file)


SOURCE_PATH = os.path.expanduser("~/Sites/ouilogique.com/_posts/blog/")
DEST_PATH = "../posts/"
FILES = os.listdir(SOURCE_PATH)
# FILES = [
#     "2015-07-02-usb_hub_test.md",
# ]

COUNT_LINKS = 0
if __name__ == "__main__":
    try:
        main()
    except SystemExit as _e:
        print(_e)
    print("DONE")
