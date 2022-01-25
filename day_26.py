new_lst = ['caroline', 'keshav', 'elenaor']
import random
student_score = {student: random.randint(1, 100) for student in new_lst}
print(student_score)
passed_student = {key: value for(key, value) in student_score.items() if value > 60}
print(passed_student)