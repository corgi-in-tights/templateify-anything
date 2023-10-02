import json
from pathlib import Path

from settings import CONFIG_DIRECTORY, CONFIG_FILE_EXTENSION 
from src.helper import get_all_paths
from src.templateify import apply_template


# get all config files
config_files = get_all_paths(CONFIG_DIRECTORY, search=f'**/*.{CONFIG_FILE_EXTENSION}')
config = {}

for cfp in config_files:
    file_path = str(cfp)
    config_file_key = cfp.name.replace(f'.{CONFIG_FILE_EXTENSION}', '').lower().replace(' ', '_')

    with open(file_path, 'r') as fp:
        config[config_file_key] = json.load(fp)


from settings import TEMPLATE_DIRECTORY, OUTPUT_DIRECTORY, PROPERTY_PATTERN, NON_SUBSTITUTE_PATHS, BLACKLISTED_PATHS, DIRECTORY_SUB_PATTERN

output_dir = Path(OUTPUT_DIRECTORY)
if (not output_dir.exists()):
    print ("Initializing output directory", output_dir)
    output_dir.mkdir(parents=True)

# move files to output if possible, substitute if can
template_files = get_all_paths(TEMPLATE_DIRECTORY)
for f in template_files:
    file_path = f.relative_to(TEMPLATE_DIRECTORY)

    apply_template(
        file_path=file_path, 
        template_dir=TEMPLATE_DIRECTORY,
        output_dir=OUTPUT_DIRECTORY,
        property_pattern=PROPERTY_PATTERN,
        directory_sub_pattern=DIRECTORY_SUB_PATTERN,
        blacklisted=BLACKLISTED_PATHS, 
        do_not_substitute=NON_SUBSTITUTE_PATHS,
        config=config,
    )
