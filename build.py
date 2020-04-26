# To build:
# 1. Install xml-patch-0.3.1.jar to the "deps" directory
# https://github.com/dnault/xml-patch
# 2. Install jinja2


from os import path
import pathlib
import re
import subprocess
import sys

import jinja2

# This isn't portable at all
# At least I feel guilty about it.
OSFE_DATA_DIRECTORY = r'C:\Program Files (x86)\Steam\steamapps\common\One Step From Eden\OSFE_Data\StreamingAssets\Data'
OSFE_SPELLS_FILE = path.join(OSFE_DATA_DIRECTORY, 'Spells.xml')
SPELLS_PATCH_TEMPLATE = r'.\src\templates\SpellsPatch.xml'
INTERMEDIATE_SPELLS_PATCH_FILE = r'.\build\SpellsPatch.xml'
SPELLS_FILE_DESTINATION = r'.\Spell Balance\Spells.xml'

XML_PATCH_JAR = r'.\deps\xml-patch-0.3.1.jar'

ITEMS_REGEX = r'itemID=\"([^\"]+)\"'
ITEMS_IN_PATCH_REGEX = r"itemID=\'([^\"]+)\'"

env = jinja2.Environment(
    autoescape=jinja2.select_autoescape(['xml']),
    loader=jinja2.FileSystemLoader(r".\src\templates\\")
)


def GetAllSpells():
    return GetAllMatches(ITEMS_REGEX, OSFE_SPELLS_FILE)

def GetAllSpellsInTemplate():
    return GetAllMatches(ITEMS_IN_PATCH_REGEX, SPELLS_PATCH_TEMPLATE)

def BuildTemplate():
    spells = GetAllSpells()
    patched_spells = set(GetAllSpellsInTemplate())
    unused_spells = [s for s in spells if s not in patched_spells]
    
    r = env.get_template('SpellsPatch.xml').render(unused_spells=unused_spells)
    with open(INTERMEDIATE_SPELLS_PATCH_FILE, 'w') as f:
        f.write(r)

def ApplyPatch():
    subprocess.run([
        'java', '-jar', XML_PATCH_JAR,
        OSFE_SPELLS_FILE, INTERMEDIATE_SPELLS_PATCH_FILE,
        SPELLS_FILE_DESTINATION
    ])

def GetAllMatches(regex, file_path):
    with open(file_path) as f:
        matches = re.findall(regex, f.read())
        print('Found {} matches'.format(len(matches)))
        return matches

def EnsureBuildDirectoryExists():
    p = pathlib.Path(r'.\build')
    p.mkdir(exist_ok=True)

# Use https://github.com/dnault/xml-patch

def main(argv):
    EnsureBuildDirectoryExists()
    BuildTemplate()
    ApplyPatch()

if __name__ == '__main__':
    main(sys.argv)