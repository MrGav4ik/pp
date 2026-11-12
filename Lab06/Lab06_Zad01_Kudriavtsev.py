# Laboratorium: 06; Zadanie 01; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

grades = []
allowed_grades = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]

allow_entering = True

grade_sum = 0
grade_average = 0
grade_max = 0
grade_min = 0

while allow_entering:
    grade = input("Wpisz ocenę w zakresie 2..5 (w skali PŁ): ")
    if grade == "0":
        allow_entering = False
    else:
        try:
            grade_float = float(grade)
            if grade_float in allowed_grades:
                grades.append(grade_float)
            else:
                print("Wpisz ocenę z zakresu [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]")
        except ValueError:
            print("Wpisz liczbę!")

if len(grades) != 0:
    for i in grades:
        grade_sum += i

    grade_average = grade_sum / len(grades)

    grade_max = max(grades)
    grade_min = min(grades)

    print("Wszystkie oceny:", grades)
    print("Najwyższa ocena:", grade_max)
    print("Najniższa ocena:", grade_min)
    print(f"Średnia ocen: {grade_average:.2f}")
else:
    print("Nie wprowadzono żadnej oceny")
