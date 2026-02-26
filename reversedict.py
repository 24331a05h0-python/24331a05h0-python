data = {"name": "sravya", "age": 20, "gender": "female"}
findvalue="sravya"
for key, value in data.items():
    if value == findvalue:
        print(key)
