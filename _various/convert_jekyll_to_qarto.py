"""

"""
import os
import shutil
from pprint import pprint
import markdown_link_extractor


def make_yaml_header_compliant(fpath):
    """___"""
    with open(fpath, "rt", encoding="utf-8") as _f:
        content = (
            _f.read().replace("comments:", "comments_:").replace("image:", "image_:")
        )
    with open(fpath, "wt", encoding="utf-8") as _f:
        _f.write(content)


def extract_img_links_and_copy_img(fpath):
    """___"""
    with open(fpath, "rt", encoding="utf-8") as _f:
        content = _f.read()
    links = markdown_link_extractor.getlinks(content)

    global COUNT_LINKS
    for link in links:
        if (
            ".tif" in link
            or ".jpg" in link
            or ".jpeg" in link
            or ".png" in link
            or ".svg" in link
        ):
            if "../../files/" in link:
                COUNT_LINKS += 1
                img_name = os.path.split(link)[-1]
                print(f"{COUNT_LINKS}. {img_name}")
                content = content.replace(link, f"./images/{img_name}")
                source_file = link.replace(
                    "../../files/", os.path.expanduser("~/Sites/ouilogique.com/files/")
                )
                dest_file
                pprint(source_file)
                shutil.copyfile(source_file, dest_file)
        break

    with open(fpath, "wt", encoding="utf-8") as _f:
        _f.write(content)
    return links


def copy_posts_from_jekyll_to_qarto():
    """___"""
    for file in FILES:
        dirname = file.split(".")[0]
        source_file = f"{SOURCE_PATH}{file}"
        dest_file = f"{DEST_PATH}{dirname}/index.qmd"
        os.makedirs(f"{DEST_PATH}{dirname}", exist_ok=True)
        shutil.copyfile(source_file, dest_file)
        make_yaml_header_compliant(dest_file)
        # extract_img_links_and_copy_img(dest_file)
        # break


def main():
    """___"""
    copy_posts_from_jekyll_to_qarto()


SOURCE_PATH = os.path.expanduser("~/Sites/ouilogique.com/_posts/blog/")
DEST_PATH = "../posts/"
FILES = os.listdir(SOURCE_PATH)
COUNT_LINKS = 0
if __name__ == "__main__":
    main()
