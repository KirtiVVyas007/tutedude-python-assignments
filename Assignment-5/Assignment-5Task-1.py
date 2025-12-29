student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 90
}
name = input("Enter the student's name: ")
if name in student_marks:
    print(name + "'s marks:", student_marks[name])
else:
    print("Student not found.")