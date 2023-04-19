student = {
    "name": "cheeku",
    "age": 24,
    "is_student": True,
    "cgpa": 9.4,
    "address": {
        "city": "rohtak",
        "pin": 124001,
    },
    "marks": [89, 98, 88, 99, 97],
    "tup": (1, 23, 4),
}

age = student["age"]
print(age)

for k, v in student.items():
    print(k, v)

copy = student.copy()
print(copy)

s = student.get("name")
print(s)

student.keys()
student.values()

student["name"] = "guddu"

print(student)
