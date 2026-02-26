student = {"name": "Sravya", "age": 19, "grade": "A+"}
print(student.keys())
print(student.values())
print(student.items())
student.pop("age")
print(student)
del student["grade"]
print(student)
