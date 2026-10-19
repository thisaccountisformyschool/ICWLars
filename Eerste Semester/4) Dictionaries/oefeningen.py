student = {"naam":"Lars",
           "leeftijd":16,
           "klas":"5ICW"
}
print(student.keys())
print(student.values())

student.update({"hobby":["Gaming","sleeping"]})
print(student)

student["leeftijd"] += 1
print(student["leeftijd"])

student.pop("klas")
print(student)

def verjaar(studentDict):
    studentDict["leeftijd"] += 1

def voeg_hobby_toe(studentDict,hobby):
    studentDict["hobby"].append(hobby)

def print_student(studentDict):
    print("Naam:", studentDict["naam"])
    print("Leeftijd:", studentDict["leeftijd"])
    print("Hobbies:", studentDict["hobby"])

verjaar(student)

verjaar(student)

print(student["leeftijd"])

voeg_hobby_toe(student,"murder")

print(student["hobby"])

print_student(student)