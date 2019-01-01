import re

secreg = re.compile(r'^\[(.+)\]$')
keyValRegEx = re.compile(r'^\s*(.+?)\s*=\s*(.+?)\s*$')
for line in open('config.ini','r'):
    found = secreg.search(line)
    if found:
        print('found a section: [%s]' % found.group(1))
    mo = keyValRegEx.search(line)
    if mo:
        print('{%s} = {%s}' % (found.group(1), mo.group(2)))


sectionRegEx = re.compile(r'^\s*\[\s*(.+?)\s*\]')
keyValRegEx = re.compile(r'^\s*(.+?)\s*=\s*(.+?)\s*$')
for lineBuf in open('config.ini', 'r'):
    mo = sectionRegEx.search(lineBuf)
    if mo:
        print('Found a section: [%s]' % mo.group(1))
    mo = keyValRegEx.search(lineBuf)
    if mo:
        print('{%s} = {%s}' % (mo.group(1), mo.group(2)))


