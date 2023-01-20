num_students = int(input("Donner le nombre d'étudiants :"))
total = 0
student_grades = []
for i in range(num_students):
    grade = float(input("Note étudiant {} : ".format(i)))
    student_grades.append(grade)
    total += grade

class_average = total / num_students
print("Moyenne de classe : {:.2f}".format(class_average))
for i in range(num_students):
    grade = student_grades[i]
    deviation = grade - class_average
    print("Numéro de l'étudiant {} | notee {} | écart à la moyenne {:.2f}")
