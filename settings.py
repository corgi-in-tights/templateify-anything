CONFIG_DIRECTORY = './config/'
CONFIG_FILE_EXTENSION = 'json'

TEMPLATE_DIRECTORY = './template/'
OUTPUT_DIRECTORY = './out/'

PROPERTY_PATTERN = r'\@{{ ([a-z._]+) }}'
DIRECTORY_SUB_PATTERN = r'\!{{ ([a-z._]+) }}'

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
