#
student_grades = {
    "Thomas": 85,
    "Blaze": 92,
    "Roderick": 52,
    "Gregory": 34
}
def calculate_average_grade(student_grades):
    total = 0
    for grades in student_grades:
       total += student_grades[grades]
    average = total / len(student_grades)
    print(average)
calculate_average_grade(student_grades)

