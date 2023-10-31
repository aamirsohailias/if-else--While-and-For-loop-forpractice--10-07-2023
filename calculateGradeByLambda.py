scores = [88, 92, 78, 95, 65]
calculate_grade = map(lambda score : 'A' if score >= 90 else ('B' if score >= 80 else ('C' if score >= 70 else 'D')),scores)
print(list(calculate_grade))
