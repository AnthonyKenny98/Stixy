"""Setup Repository."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-05-04 17:28:33
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-05-05 08:31:54


from os.path import dirname, abspath
from os import walk, listdir
import re

# Filepath constants
FILE_DIR = dirname(abspath(__file__))
TOP_LEVEL_DIR = dirname(dirname(dirname(FILE_DIR)))
PLACEHOLDER_VALUES_DIR = FILE_DIR + '/placeholder_values'

# Define Markdown Wrappers
MD_PH_BEGIN = '<!--- DO NOT REMOVE Begin:{} --->'
MD_PH_END = '<!--- DO NOT REMOVE End:{} --->'

# Global Data structures
MARKDOWN_FILES = []
DICTIONARY = {}


# Check top level directory
# proceed = input('''
# Please confirm that this is the top level directory of your repository:\n
# {}\n
# Confirm (y/n)? '''.format(TOP_LEVEL_DIR))

# while proceed not in ['y', 'n', 'Y', 'N']:
#     proceed = input('Confirm (y/n)? ')
# if proceed in ['n', 'N']:
#     print("Incorrect Top Level Directory, please update this script.")
#     exit()

# Find all markdown files
for root, _, files in walk(TOP_LEVEL_DIR):
    for file in files:
        if file.endswith('.md') and '.' not in root:
            MARKDOWN_FILES.append(root + '/' + file)

# Load dictionary of placeholder values
for file in listdir(PLACEHOLDER_VALUES_DIR):
    if file.endswith('.txt'):
        with open(PLACEHOLDER_VALUES_DIR + '/' + file) as f:
            value = f.read()
            if value != '':
                DICTIONARY[file.strip('.txt')] = value


def replace_placeholders(filepath):
    """Function to replace MD placeholders with values from dictionary."""
    with open(filepath) as f:
        contents = f.read()

    for placeholder, value in DICTIONARY.items():
        md_ph_begin = MD_PH_BEGIN.format(placeholder)
        md_ph_end = MD_PH_END.format(placeholder)

        try:
            contents = re.sub(
                '{}([\s\S]*?){}'.format(md_ph_begin, md_ph_end),
                '{}\n{}\n\n{}'.format(md_ph_begin, value, md_ph_end),
                contents,
                flags=re.DOTALL)
        except AttributeError:
            pass

    with open(filepath, 'w') as f:
        f.write(contents)

for file in MARKDOWN_FILES:
    replace_placeholders(file)
