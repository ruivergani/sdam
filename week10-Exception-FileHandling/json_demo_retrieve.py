import json

# retrive data from json file
with open('char_classes.json', 'r') as f:
    class_data = json.load(f)

for name, stats in class_data.items():
    print(name.capitalize(), end=' :: ')
    print('str: {}, int: {}, wis: {}, dex: {}, con: {}'.format(
        stats['str'], stats['int'], stats['wis'], stats['dex'], stats['con']
    ))
    print('*' * 10)
