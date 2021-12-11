import json

with open('resources/char_classes.json', 'r') as f:
    class_data = json.load(f)

for name, stats in class_data.items():
    print(name.capitalize(), end=' :: ')
    print('str: {}, int: {}, wis: {}, dex: {}, con: {}'.format(
        stats['str'], stats['int'], stats['wis'], stats['dex'], stats['con']
    ))
    print('*' * 10)
