CONFIG_DIRECTORY = './config/'
CONFIG_FILE_EXTENSION = 'json'

TEMPLATE_DIRECTORY = './template/'
OUTPUT_DIRECTORY = './out/'

# patterns - @{{ mytext }} and !{{ mytext }}
PROPERTY_PATTERN = r'\@{{ ([a-z._]+) }}'
DIRECTORY_SUB_PATTERN = r'\!{{ ([a-z._]+) }}'


# if enabled, all values are stored in the same global module (but also regularly)
# throws an error if there are any conflicting property ids
# 
# causes values with no module specified (ie instead of `b.test_property`, just `test_property`) 
# to function
DEFAULT_GLOBAL_MODULE = True

NON_SUBSTITUTE_PATHS = [
    r'LICENSE',
    r'README.md',
    r'(.+).png',

    r'unsubbed_file.java'
]

BLACKLISTED_PATHS = [
    r'DS_Store',
    r'^ignoredfile.txt$',
    r'my_contents_are_ignored/.+'
]
