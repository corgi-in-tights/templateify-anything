import os
import json
import re
import shutil

from pathlib import Path
from typing import Dict, Union, List

from .helper import is_path_in_rule_set


def get_prop_value(property_path: str, config: Dict[str, Union[dict, str]], use_global_namespace: bool = False):
    # we want to get the bottom-most parent (or throw an error)

    # split to array
    prop = property_path.split('.')

    if (len(prop) == 1):
        if (use_global_namespace):
            if (prop[0] in config['global']):
                return config['global'][prop[0]]
            raise KeyError(f'Property "{property_path}" not found in global module (no module specified).')
        raise KeyError(f'Property "{property_path}" requires a module i.e. `mymodule.{property_path}`!')
    
    # start at top
    parent = config
    # get first item on path
    current_item = prop.pop(0)

    while current_item in parent:  # is item in config?
        if (len(prop) != 0):  # are there more items
            parent = parent[current_item]  # iterate downwards
            current_item = prop.pop(0)
        else:  # no more items remaining
            break

    if (not current_item in parent):
        raise KeyError(f'Cannot find property "{property_path}" in config!')
    return parent[current_item]



def find_and_substitute_props(s: str, property_pattern: re.Pattern, config, search_function=re.search, substitute_function=re.sub, use_global_namespace: bool = False):
    m = search_function(property_pattern, s)
    if (m): # it has a property
        property_path = m.group(1)
        val = get_prop_value(property_path, config, use_global_namespace=use_global_namespace)

        # now substitute values
        return substitute_function(property_pattern, val, s)
    return s

def substitute_properties(template_file_path: Path, output_file_path: Path, config: Dict[str, Union[dict, str]], property_pattern: re.Pattern=r'\${{ ([a-z._]+) }}', directory_sub_pattern: re.Pattern=r'\!{{ ([a-z._]+) }}', use_global_namespace: bool = False):
    # print ('Substituting values.')

    with open(template_file_path, 'r') as fp:
        lines = fp.readlines()
        new_lines = [find_and_substitute_props(line, property_pattern, config, use_global_namespace=use_global_namespace) for line in lines]

    with open(output_file_path, 'w') as fp:
        fp.writelines(new_lines)

def multi_substitute(basic_output_file_path: Path, directory_sub_pattern: re.Pattern, config, use_global_namespace: bool = False):
    def dir_search_func(pattern, val):
        return re.match(pattern, val)
    
    def dir_substitute_function(pattern, val, s):
        return re.sub(pattern, val.replace('.', '/'), s)
    
    new_string_path = ''
    parts = basic_output_file_path.parts
    
    for slug in parts:
        new_string_path += find_and_substitute_props(s=slug, property_pattern=directory_sub_pattern, config=config, search_function=dir_search_func, substitute_function=dir_substitute_function, use_global_namespace=use_global_namespace) + '/'

    new_dir_path = Path(new_string_path)
    return new_dir_path




def copy_file(template_file_path: Path, output_file_path: Path):
    shutil.copyfile(str(template_file_path), str(output_file_path), follow_symlinks=True)



def apply_template(file_path: Path, template_dir: Path, output_dir: Path, property_pattern, directory_sub_pattern, blacklisted: List[re.Pattern], do_not_substitute: List[re.Pattern], config, use_global_namespace: bool = False):    
    template_file_path = template_dir / file_path
    
    # apply basic properties substitutions (change name)
    basic_output_file_path = Path(find_and_substitute_props(str(file_path), property_pattern, config, use_global_namespace=use_global_namespace))

    # apply directory property substitutions (change name and create if needed)
    output_file_path = output_dir / multi_substitute(basic_output_file_path, directory_sub_pattern, config, use_global_namespace=use_global_namespace)

    # should file be avoided
    if (is_path_in_rule_set(file_path, blacklisted)):
        # print (template_file_path, 'is blacklisted! Skipping.')
        return
    

    # print ('Moving', template_file_path, 'to', output_file_path)

    # if directory
    if (template_file_path.is_dir()): 
        output_file_path.mkdir(parents=True, exist_ok=True)
        return
    else:
        Path('/'.join(output_file_path.parts[:-1])).mkdir(parents=True, exist_ok=True)

    # skip substitutions if part of ruleset
    if (is_path_in_rule_set(file_path, do_not_substitute)):
        # print ('Skipping substitutions')
        copy_file(template_file_path, output_file_path)
        return


    substitute_properties(
        template_file_path=template_file_path,
        output_file_path=output_file_path,
        config=config,
        property_pattern=property_pattern,
        directory_sub_pattern=directory_sub_pattern,
        use_global_namespace=use_global_namespace
    )


