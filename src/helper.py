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