"""

"""
import os
import shutil
import traceback
from pprint import pprint

import json
import markdown_link_extractor
import yaml


def copy_posts_from_jekyll_to_quarto(source_file, dest_dir, dest_file):
    """___"""
    os.makedirs(f"{dest_dir}", exist_ok=True)
    shutil.copyfile(source_file, dest_file)


def make_yaml_header_compliant(fpath):
    """___"""

    yaml_header, content = readyaml_header(fpath)
    yaml_header = yaml.safe_load(yaml_header)
    if yaml_header["image"]["feature"]:
        yaml_header["image"] = f'./images/{yaml_header["image"]["feature"]}'
    else:
        del yaml_header["image"]
    yaml_header["draft"] = not yaml_header["published"]
    del yaml_header["published"]
    yaml_header["categories"] = yaml_header["tags"]
    del yaml_header["tags"]

    new_fpath = "/" + fpath[len("../posts/") + len("2015-05-21-") : fpath.rfind("/")]
    # print(new_fpath)
    yaml_header["aliases"] = yaml_header["redirect_from"]
    yaml_header["aliases"] += [new_fpath]
    del yaml_header["redirect_from"]
    yaml_header["pagetitle"] = "{{< meta title >}} &#8211; ouilogique.com"
    yaml_header["filters"] = ["lightbox"]
    yaml_header["lightbox"] = "auto"

    yaml_header = (
        f"---\n{yaml.safe_dump(yaml_header, allow_unicode=True, indent=4, width=4)}---\n"
    )
    content = yaml_header + content
    # print(content)
    # raise SystemExit
    with open(fpath, "wt", encoding="utf-8") as _f:
        _f.write(content)


def remove_style_from_img(dest_dir, dest_file):
    """___"""
    content = ""
    with open(dest_file, "rt", encoding="utf-8") as _f:
        for line in _f.readlines():
            pos1 = line.find('{:')
            if pos1 > -1:
                pos2 = line.find('}', pos1)
                if pos2 > -1:
                    new_line = line[:pos1] + line[pos2+1:] + "\n"
                    print(line)
                    print(new_line)
                    print(line[pos1:pos2+1])
                    content += new_line
            else:
                content += line

    with open(dest_file, "wt", encoding="utf-8") as _f:
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
                # if not os.path.exists(source_img_path):
                #     raise SystemExit(f"{source_img_path} not found")
                if os.path.exists(source_img_path):
                    shutil.copyfile(source_img_path, dest_img_path)
                else:
                    print(f"{source_img_path} not found")

                # print(f"{COUNT_LINKS}. {source_img_path}")
                # print(dest_img_path)

    with open(dest_file, "wt", encoding="utf-8") as _f:
        _f.write(content)

    return links


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


def extract_feature_img_links_and_copy_img(dest_dir, dest_file):
    """___"""
    yaml_header, _ = readyaml_header(dest_file)

    img_feature = None
    feature_img_path = None
    try:
        yaml_header = yaml.safe_load(yaml_header)
        img_feature = yaml_header["image"]
        if img_feature is None or len(img_feature) == 0:
            raise KeyError(
                "Le champ `image_/feature` n’existe pas dans le fichier YAML."
            )
        feature_img_dir = os.path.expanduser("~/Sites/ouilogique.com/")
        feature_img_path = f"{feature_img_dir}{img_feature}"
    except KeyError:
        pass
    except TypeError:
        pass
    else:
        dest_img_dir = f"{dest_dir}"
        os.makedirs(dest_img_dir, exist_ok=True)
        dest_img_path = f"{dest_img_dir}/{img_feature}"

        if os.path.exists(feature_img_path):
            # print("#######")
            # print(f"feature_img_path = {feature_img_path}")
            # print(f"dest_img_path = {dest_img_path}")
            # print(f"dest_dir = {dest_dir}")
            # print("#######")

            shutil.copyfile(feature_img_path, dest_img_path)
            # raise SystemExit(f"{feature_img_path} not found")
            # with open(dest_file, "rt", encoding="utf-8") as _f:
            #     content = _f.read().replace(img_feature, f"./toto/{img_feature}")
            # with open(dest_file, "wt", encoding="utf-8") as _f:
            #     _f.write(content)
            # print(f"{feature_img_path} found")
        else:
            print(f"{feature_img_path} not found")


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
    files = sorted(os.listdir(SOURCE_PATH_POSTS), reverse=True)

    # ref_keys = {
    #     "author",
    #     # "categories",
    #     # "comments",
    #     "date",
    #     # "excerpt",
    #     "image",
    #     "lang",
    #     "layout",
    #     # "modified",
    #     "published",
    #     "redirect_from",
    #     # "share",
    #     "tags",
    #     "title",
    # }
    # all_keys = ref_keys
    for file in files:
        fpath = f"{SOURCE_PATH_POSTS}{file}"
        yaml_header, _ = readyaml_header(fpath)
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

    dirs = sorted(os.listdir(f"{SOURCE_PATH}files/"), reverse=True)
    dirs = [f"{SOURCE_PATH}files/{dir}" for dir in dirs if dir not in [".DS_Store"]]
    for dir in dirs:
        dest_path = f"{DEST_PATH}posts/{os.path.split(dir)[1]}"
        shutil.copytree(dir, dest_path, dirs_exist_ok=True)
    # raise SystemExit

    dirs = [
        f"{SOURCE_PATH}enum",
        f"{SOURCE_PATH}radios",
        f"{SOURCE_PATH}scratchpad",
    ]
    # pprint(dirs)
    for dir in dirs:
        dest_path = f"{DEST_PATH}pages/{os.path.split(dir)[1]}"
        shutil.copytree(dir, dest_path, dirs_exist_ok=True)
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
    content = ""
    with open(dest_file, "rt", encoding="utf-8") as _f:
        for line in _f:
            pos1 = line.find("../../files")
            if pos1 > -1:
                pos2 = line.find(")", pos1)
                link = line[pos1:pos2]
                link = os.path.split(link)[-1]
                new_line = line[:pos1] + "./docs/" + link + line[pos2:]
                # print(link)
                # print(line)
                # print(new_line)
                # print("#############\n\n\n\n\n")
                line = new_line
            line = line.replace(
                "[Introduction au langage HTML]: ../introduction-html/",
                "[Introduction au langage HTML]: ../2018-02-15-introduction-html/",
            )
            line = line.replace(
                "[Introduction au langage CSS]: ../introduction-css/",
                "[Introduction au langage CSS]: ../2018-02-16-introduction-css/",
            )
            line = line.replace(
                "[Introduction au langage JavaScript]: ../introduction-javascript/",
                "[Introduction au langage JavaScript]: ../2018-02-17-introduction-javascript/",
            )
            line = line.replace("../pinouts/", "../2015-05-28-pinouts/")
            line = line.replace(
                "../installer-raspian-stretch/",
                "../2023-03-09-installer-raspberry-pi-os-sur-raspberry-pi-sans-clavier-ni-souris-ni-ecran/",
            )
            line = line.replace(
                "../installer-raspberry-pi-os-sur-raspberry-pi-sans-clavier-ni-souris-ni-ecran/",
                "../2023-03-09-installer-raspberry-pi-os-sur-raspberry-pi-sans-clavier-ni-souris-ni-ecran/",
            )
            line = line.replace(
                "[../esp_commandes_at_utiles/](../esp_commandes_at_utiles/)",
                "[../2016-08-13-esp_commandes_at_utiles/](../2016-08-13-esp_commandes_at_utiles/)",
            )
            # line = line.replace("", "")
            # line = line.replace("", "")
            content += line

    with open(dest_file, "wt", encoding="utf-8") as _f:
        _f.write(content)

    return

    # links = content.find()

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


def inject_js(dest_file):
    """___"""
    # print(dest_file)
    if not os.path.exists(dest_file):
        print(f"{dest_file} does not exists")
        return

    with open(dest_file, "rt", encoding="utf-8") as _f:
        content = _f.read()
    content += """
<script src="/js/prev_next_links.js"></script>
<script src="/js/prev_next_buttons.js"></script>

"""

    with open(dest_file, "wt", encoding="utf-8") as _f:
        _f.write(content)


def create_prev_next_links_js():
    """___"""

    non_draft_files = []
    for file in FILES:
        dirname = file.split(".")[0]
        dest_dir = f"{DEST_PATH_POSTS}{dirname}/"
        dest_file = f"{dest_dir}index.qmd"
        if not os.path.exists(dest_file):
            raise SystemExit(f"{dest_file} does not exists")
        yaml_header, _ = readyaml_header(dest_file)
        yaml_header = yaml.safe_load(yaml_header)
        if not yaml_header["draft"]:
            non_draft_files.append(dest_file)

    prev_next_links = []
    home_url = "../../"
    for id, _file in enumerate(sorted(non_draft_files, reverse=True)):
        inject_js(_file)
        _next = f"../{non_draft_files[id - 1]}" if id > 0 else home_url
        _prev = (
            f"../{non_draft_files[id + 1]}"
            if id < len(non_draft_files) - 1
            else home_url
        )
        _prev = _prev.replace("/index.qmd", "").replace("../../posts/", "../")
        _next = _next.replace("/index.qmd", "").replace("../../posts/", "../")
        _file = os.path.split(os.path.split(_file)[0])[-1].replace(".md", "")
        prev_next_links.append(
            {
                "curr": _file,
                "prev": _prev,
                "next": _next,
            }
        )

    prev_next_links_json = json.dumps(prev_next_links, indent=4)

    fpath = "../js/prev_next_links.js"
    with open(fpath, "wt", encoding="utf-8") as _f:
        _f.write("prev_next_links = ")
        _f.write(prev_next_links_json)


def main():
    """___"""
    copy_individual_files()
    create_nojekyll()
    for file in FILES:
        dirname = file.split(".")[0]
        source_file = f"{SOURCE_PATH_POSTS}{file}"
        dest_dir = f"{DEST_PATH_POSTS}{dirname}/"
        dest_file = f"{dest_dir}index.qmd"
        copy_posts_from_jekyll_to_quarto(source_file, dest_dir, dest_file)
        make_yaml_header_compliant(dest_file)
        extract_img_links_and_copy_img(dest_dir, dest_file)
        remove_style_from_img(dest_dir, dest_file)
        extract_feature_img_links_and_copy_img(dest_dir, dest_file)
        adapt_links(dest_file)

    # create_prev_next_links_js()


SOURCE_PATH = os.path.expanduser("~/Sites/ouilogique.com/")
SOURCE_PATH_POSTS = os.path.expanduser("~/Sites/ouilogique.com/_posts/blog/")
DEST_PATH = "../"
DEST_PATH_POSTS = "../posts/"
FILES = sorted(os.listdir(SOURCE_PATH_POSTS), reverse=True)
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
        pprint(_e)
        traceback.print_exc()

    print("DONE")
