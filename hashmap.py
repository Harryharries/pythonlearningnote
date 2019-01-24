student = {"name":"harry","age":21,"course":["comp3010","comp2020"]}
student["new"] = "hhh"
print(student.keys())
print(student.values())
print(student.items())
del student["name"]
print(student.items())

for k in student.items():
    print(k)

name = "acddd"
name = name[0:]
print(name)
print(name.index('a'))

