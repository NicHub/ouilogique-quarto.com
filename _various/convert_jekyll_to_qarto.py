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
            # .replace("comments:", "comments_:")
            .replace("    feature:", "image:").replace("image:\n", 'image: ""\n')
        )
    content = content.replace('image: ""\nimage: ', "image: ")
    content = content.replace("image: null", 'image: ""')
    content = content.replace('image: ""\n', "")
    content = content.replace("redirect_from", "aliases")
    content = content.replace("published: false", "draft: true")
    content = content.replace("published: true", "draft: false")
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
                # print(f"{COUNT_LINKS}. {source_img_path}")
                # print(dest_img_path)

    with open(dest_file, "wt", encoding="utf-8") as _f:
        _f.write(content)

    return links


def readyaml_header(file_path):
    """___"""
    yaml_header = ""
    cnt = 0
    with open(file_path, "rt", encoding="utf-8") as _f:
        for line in _f:
            if cnt == 2:
                break
            if line[:3] == "---":
                cnt += 1
                continue
            yaml_header += line
    return yaml_header


def extract_feature_img_links_and_copy_img(dest_dir, dest_file):
    """___"""
    yaml_header = readyaml_header(dest_file)
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


def write_jekyll_yaml_header(file, yaml_header, line_cnt):
    """___"""
    content = ""
    cnt = -1
    with open(file, "rt", encoding="utf-8") as _f:
        for line in _f:
            cnt += 1
            if cnt < line_cnt:
                continue
            content += line

    yaml_string = yaml.safe_dump(
        yaml_header, default_flow_style=False, allow_unicode=True
    )
    content = "---\n" + yaml_string + "---\n" + content
    # pprint(content)
    with open(file, "wt", encoding="utf-8") as _f:
        _f.write(content)

    pprint(yaml_header)
    pprint(yaml.safe_load(yaml_string))


def compare_jekyll_post_metadata():
    """___"""
    files = os.listdir(SOURCE_PATH_POSTS)

    ref_keys = {
        "author",
        # "categories",
        # "comments",
        "date",
        # "excerpt",
        "image",
        "lang",
        "layout",
        # "modified",
        "published",
        "redirect_from",
        # "share",
        "tags",
        "title",
    }
    # all_keys = ref_keys
    for file in files:
        fpath = f"{SOURCE_PATH_POSTS}{file}"
        yaml_header = readyaml_header(fpath)
        line_cnt = yaml_header.count("\n") + 1 + 1
        yaml_header = yaml.safe_load(yaml_header)
        keys = set(yaml_header.keys())
        # all_keys = set(all_keys.union(keys))
        # elements_manquants = all_keys.difference(keys)
        # if elements_manquants:
        #     print("")
        #     print(file)
        #     print(elements_manquants)
        if "redirect_from" not in keys:
            yaml_header["redirect_from"] = None
            # print("")
            # print(file)

        # if not all_keys == keys:
        #     pprint(file)
        #     pprint(keys)
        #     pprint(all_keys)
        write_jekyll_yaml_header(fpath, yaml_header, line_cnt)
        # raise SystemExit()

    # pprint(all_keys)


def copy_individual_files():
    """___"""

    dirs = os.listdir(f"{SOURCE_PATH}files/")
    dirs = [f"{SOURCE_PATH}files/{dir}" for dir in dirs if dir not in [".DS_Store"]]
    dirs += [
        f"{SOURCE_PATH}enum",
        f"{SOURCE_PATH}radios",
        f"{SOURCE_PATH}scratchpad",
    ]
    for dir in dirs:
        shutil.copytree(dir, f"{DEST_PATH}{dir}", dirs_exist_ok=True)
    # pprint(dirs)
    # raise SystemExit

    files = [
        "favicon.ico",
        "favicon.png",
        "LICENSE",
    ]
    for file in files:
        shutil.copyfile(f"{SOURCE_PATH}{file}", f"{DEST_PATH}{file}")


def create_nojekyll():
    """___"""
    with open("../.nojekyll", "wt", encoding="utf-8") as _f:
        _f.write("")


def adapt_links(dest_file):
    """___"""

    with open(dest_file, "rt", encoding="utf-8") as _f:
        content = _f.read()
    # fmt: off
    replacements = [
        ["/installer-raspian-stretch/"                                                                            , "2020-12-25-installer-pi-hole-sur-un-raspberry"],
        # ["/2019-03-27-plateforme-de-stewart-esp32/images/images/2021-04-24-proto-plateforme-de-stewart_001.jpg"   , ""],
        ["/introduction-html/"                                                                                    , "/2018-02-15-introduction-html/"],
        ["/introduction-css/"                                                                                     , "/2018-02-16-introduction-css/"],
        ["/introduction-javascript/"                                                                              , "/2018-02-17-introduction-javascript/"],
        ["/pinouts/"                                                                                              , "/2015-05-28-pinouts/"],
        # ["/posts/2015-11-01-Strinity_Sensors_Cobber/images/images/Strinity_Sensors_Cobber_001.jpg"                      , ""],
    ]
    # fmt: on
    for replacement in replacements:
        if replacement[0] in content:
            print(f"{dest_file} {replacement[0]}")
            content = content.replace(replacement[0], replacement[1])
    with open(dest_file, "wt", encoding="utf-8") as _f:
        _f.write(content)


def main():
    """___"""
    copy_individual_files()
    create_nojekyll()
    for file in FILES:
        dirname = file.split(".")[0]
        source_file = f"{SOURCE_PATH_POSTS}{file}"
        dest_dir = f"{DEST_PATH_POSTS}{dirname}/"
        dest_file = f"{dest_dir}index.qmd"
        copy_posts_from_jekyll_to_qarto(source_file, dest_dir, dest_file)
        make_yaml_header_compliant(dest_file)
        extract_img_links_and_copy_img(dest_dir, dest_file)
        extract_feature_img_links_and_copy_img(dest_dir, dest_file)
        # adapt_links(dest_file)


SOURCE_PATH = os.path.expanduser("~/Sites/ouilogique.com/")
SOURCE_PATH_POSTS = os.path.expanduser("~/Sites/ouilogique.com/_posts/blog/")
DEST_PATH = "../"
DEST_PATH_POSTS = "../posts/"
FILES = os.listdir(SOURCE_PATH_POSTS)
# FILES = [
#     "2019-03-27-plateforme-de-stewart-esp32.md",
# ]

COUNT_LINKS = 0
if __name__ == "__main__":
    # try:
    #     compare_jekyll_post_metadata()
    # except SystemExit as _e:
    #     print(_e)
    # print("DONE")

    try:
        main()
    except SystemExit as _e:
        print(_e)
    print("DONE")
