# student_grade.py

name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)