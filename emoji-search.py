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
    if search_term in emoji_name:
        item = SubElement(top, 'item', {'uid': emoji_name, 'arg': emoji_description['char']})
        icon = SubElement(item, 'icon')
        icon.text = 'icon.png'
        title = SubElement(item, 'title')
        title.text = emoji_description['char']
        subtitle = SubElement(item, 'subtitle')
        subtitle.text = "Paste \'{}\'  at cursor.".format(emoji_name)
    for keyword in emoji_description['keywords']:
        if search_term in keyword:
            item = SubElement(top, 'item', {'uid': emoji_name, 'arg': emoji_description['char']})
            icon = SubElement(item, 'icon')
            icon.text = 'icon.png'
            title = SubElement(item, 'title')
            title.text = emoji_description['char']
            subtitle = SubElement(item, 'subtitle')
            subtitle.text = "Paste \'{}\'  at cursor.".format(emoji_name)

print(tostring(top, encoding="unicode"))
