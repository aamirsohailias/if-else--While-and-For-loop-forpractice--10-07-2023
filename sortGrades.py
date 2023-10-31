grades = {'Alice': 88, 'Bob': 92, 'Charlie': 78, 'David': 95}
sorted_grades = dict(sorted(grades.items(), key=lambda x: x[1], reverse=True))
print(sorted_grades)