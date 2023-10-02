import json
from pathlib import Path

from src.helper import get_all_paths
from src.config import create_config
from src.templateify import apply_template


from settings import CONFIG_DIRECTORY, CONFIG_FILE_EXTENSION, DEFAULT_GLOBAL_MODULE

config = create_config(Path(CONFIG_DIRECTORY), CONFIG_FILE_EXTENSION, DEFAULT_GLOBAL_MODULE)



from settings import TEMPLATE_DIRECTORY, OUTPUT_DIRECTORY, PROPERTY_PATTERN, NON_SUBSTITUTE_PATHS, BLACKLISTED_PATHS, DIRECTORY_SUB_PATTERN, DEFAULT_GLOBAL_MODULE

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
        use_global_namespace=DEFAULT_GLOBAL_MODULE
    )
