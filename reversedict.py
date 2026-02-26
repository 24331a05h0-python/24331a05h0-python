data = {"name": "sravs", "age": 20, "gender": "female"}
value_to_find="sravs"
for key, value in data.items():
    if value == value_to_find:
        print(key)
