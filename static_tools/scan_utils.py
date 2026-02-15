import os
import re


ALLOWED_EXTENSIONS = (".java", ".kt", ".xml", ".smali")


def is_valid_source_file(path):

    if not os.path.isfile(path):
        return False

    return path.endswith(ALLOWED_EXTENSIONS)


def remove_comments(code):

    # Java / Kotlin
    code = re.sub(r"//.*", "", code)
    code = re.sub(r"/\*[\s\S]*?\*/", "", code)

    # XML
    code = re.sub(r"<!--[\s\S]*?-->", "", code)

    return code


def load_whitelist():

    file = os.path.join(
        os.path.dirname(__file__),
        "whitelist.txt"
    )

    if not os.path.exists(file):
        return []

    with open(file) as f:
        return [line.strip() for line in f]
