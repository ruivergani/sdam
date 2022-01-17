#  code example for nested dictionary

# iterate through a nested dictionary

people = {
        1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
        2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}
}

for key_id, value_id in people.items():
    print("\nPerson ID: ", key_id)

    for key in value_id:
        print(key + ':', value_id[key])