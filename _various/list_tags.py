from pprint import pprint
import yaml

SOURCE_PATH = os.path.expanduser("~/Sites/ouilogique.com/")
SOURCE_PATH_POSTS = os.path.expanduser("~/Sites/ouilogique.com/_posts/blog/")
DEST_PATH = "../"
DEST_PATH_POSTS = "../posts/"
FILES = os.listdir(SOURCE_PATH_POSTS)


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


if __name__ == "__main__":
    for file in FILES:
        list_tags(f"{SOURCE_PATH_POSTS}{file}")
    pprint(UNIQUE_TAGS)