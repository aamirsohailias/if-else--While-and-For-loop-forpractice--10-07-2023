def find_average_marks(marks):
    # marks = [55, 64, 75, 80, 34]
    total_subjects = len(marks)
    sum_of_marks = sum(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks
def find_grade(average_marks):
    if average_marks > 80:
        grade = "A"
    elif average_marks > 70:
        grade = "B"
    elif average_marks > 60:
        grade = "c"
    else:
        grade = "F"
    return grade
marks = [55, 64, 75, 80, 95]
# average_marks = find_average_marks(marks
print("your average marks is: ", find_average_marks(marks))
grade = find_grade(find_average_marks(marks))
print("Your grade is: ", grade)