import json
import os
folder=os.path.dirname(__file__)
path=os.path.join(folder,"student.json")
def save_data():
    with open(path, "w") as f:
        json.dump(students,f, indent=2)
def load_data():
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
students=load_data()
def add_student():
    try:
        roll=int(input("Enter your roll no: "))
    except ValueError:
        print("Please enter a valid roll no ")
        return
    if roll in [s["Roll"] for s in students]:
        print("Student already exists")
        return
    name=input("Enter your name: ")
    try:
        class_name=int(input("Enter your Class: "))
    except ValueError:
        print("Please enter a valid class ")
        return
    try:
        marks=int(input("Enter your marks: "))
    except ValueError:
        print("Please enter a valid marks ")
        return
    students.append({"Roll":roll, "Name":name, "Class":class_name, "Marks":marks})
    save_data()
    print("Student added successfully")
def view_student():
    if len(students)==0:
        print("No students found")
    else:
        for student in students:
            print(f" Roll No: {student['Roll']}, Name: {student['Name']}, Class: {student['Class']}, Marks: {student['Marks']}")
def edit_student():
    roll=int(input("Enter the roll no of the student you want to edit: "))
    for student in students:
        if student["Roll"]==roll:
            student["Name"]=input("Enter the new name: ")
            student["Class"]=int(input("Enter the new class: "))
            student["Marks"]=int(input("Enter the new marks: "))
            save_data()
            print("Student updated successfully")
            return
    print("Student not found")
def delete_student():
    roll=int(input("Enter the roll no of the student you want to delete: "))
    for student in students:
        if student["Roll"]==roll:
            students.remove(student)
            save_data()
            print("Student deleted successfully")
            return
    print("Student not found")
#menu
while True:
    print(""" 
    1 for add student
    2 for view student
    3 for edit student
    4 for delete student
    5 for exit """)
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice ")
        continue
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        edit_student()
    elif choice==4:
        delete_student()
    elif choice==5:
        break
    else:
        print("Please enter a valid choice ")
    