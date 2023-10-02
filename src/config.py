import json
from pathlib import Path

from .helper import get_all_paths, flat_list_to_nested_dict


def create_config(directory_path, file_extension, use_global_namespace):
    # get all config files
    config_files = get_all_paths(
        directory_path, search=f'**/*.{file_extension}')
    if (use_global_namespace):
        config = {'global': {}}
    else:
        config = {}

    for f in config_files:
        file_path = str(f)
        config_file_key = f.name.replace(
            f'.{file_extension}', '').lower().replace(' ', '_')

        with open(file_path, 'r') as fp:
            data = json.load(fp)
            config[config_file_key] = data

            if (use_global_namespace):
                g = config['global']
                for k, v in data.items():
                    if (k in g):
                        raise KeyError(f'Key "{k}" already in global config!')
                    config['global'][k] = v

    return config
