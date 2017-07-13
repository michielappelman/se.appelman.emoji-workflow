#!/usr/bin/python
# vim: set fileencoding=utf8 :

import json
import sys
from xml.etree.ElementTree import Element, SubElement, tostring

# From https://raw.githubusercontent.com/muan/emojilib/master/emojis.json
EMOJI_FILE = "emojis.json"

with open(EMOJI_FILE, 'r') as emoji_file:
    emoji_json = json.load(emoji_file)

search_term = sys.argv[1]

top = Element('items')
for emoji_name, emoji_description in emoji_json.items():
    if len(list(top)) > 24:
        continue
    if search_term in emoji_name and emoji_description['char']:
        item = SubElement(top, 'item', {'uid': emoji_name, 'arg': emoji_description['char']})
        icon = SubElement(item, 'icon')
        icon.text = 'icon.png'
        title = SubElement(item, 'title')
        title.text = emoji_description['char']
        subtitle = SubElement(item, 'subtitle')
        subtitle.text = "Paste \'{}\'  at cursor.".format(emoji_name)
    for keyword in emoji_description['keywords']:
        if search_term in keyword and emoji_description['char']:
            item = SubElement(top, 'item', {'uid': emoji_name, 'arg': emoji_description['char']})
            icon = SubElement(item, 'icon')
            icon.text = 'icon.png'
            title = SubElement(item, 'title')
            title.text = emoji_description['char']
            subtitle = SubElement(item, 'subtitle')
            subtitle.text = "Paste \'{}\'  at cursor.".format(emoji_name)

if len(list(top)) == 0:
        item = SubElement(top, 'item', {'uid': 'missing', 'arg': 'missing'})
        icon = SubElement(item, 'icon')
        icon.text = 'frowning.png'
        title = SubElement(item, 'title')
        title.text = u"Nope... 🙁"
        subtitle = SubElement(item, 'subtitle')
        subtitle.text = "No matching emoji found..."

print(tostring(top, encoding="utf8"))
