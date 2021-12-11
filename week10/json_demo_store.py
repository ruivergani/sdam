import json

classes = {
    "warrior": {"str": 15, "int": "-", "wis": "-", "dex": 12, "con": 10},
    "wizard": {"str": "-", "int": 15, "wis": 10, "dex": 10, "con": "-"},
    "thief": {"str": 10, "int": 9, "wis": "-", "dex": 15, "con": "-"},
    "necromancer": {"str": 10, "int": 10, "wis": 15, "dex": "-", "con": "-"}
}

json_string = json.dumps(classes, indent=2)

print(json_string)

with open('resources/char_classes.json', 'w') as f:
    json.dump(classes, f, indent=2)
