import re
from pathlib import Path
from typing import List


def get_all_paths(directory_path: str, search: str = '*'):
    return Path(directory_path).rglob(search)


def is_path_in_rule_set(file_path: str, rules: List[re.Pattern]):
    for r in rules:
        if (re.search(r, str(file_path))):
            return True
    return False


def flat_list_to_nested_dict(arr):
    if (len(arr) < 1):
        return {} # not enough elements
    
    new_latest_dict = {arr[-2]: arr[-1]}

    for i in range(3, len(arr) + 1):
        new_latest_dict = {arr[-i]: new_latest_dict}

    return new_latest_dict