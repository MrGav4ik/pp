# Laboratorium: 07; Zadanie 04; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

running = True

database = {
    "Anna": [5, 4, 6],
    "Bartek": [2, 3, 5],
    "Celina": [5, 5, 5],
    "Dawid": [2, 2, 3],
}

avg_students = {}

def add_student(data, name, grades_str):
    try:
        grades = list(map(int, grades_str.split(" "))) # Zakładam, że oceny są liczbami całkowitymi
        data[name] = grades
        output = {"msg": "Nowy uczeń jest dodany", "name": name, "grades": grades}
    except ValueError:
        output = {"msg": "Nie poprawny format oceny"}
    return output

def avg_student(data, name):
    grades = data[name]
    sum = 0
    for i in grades: sum += i
    avg = sum / len(grades)    
    return avg

def best_student(data):
    for name in data.keys():
        avg = avg_student(data, name)
        avg_students[name] = round(avg, 2)
    max_avg = max(avg_students, key=avg_students.get)
    return max_avg, avg_students[max_avg]

def menu(data):
    choice = int(input("Wprowadż wybór: 1 - dodać ucznia, 2 - średnia ucznia, 3 - najlepszy uczeń, 0 - zakończyć: "))
    match choice:
        case 0:
            global running
            running = False
        case 1:
            name = input('Wprowadź imię ucznia (lub "stop" by zakończyć): ')
            if name != "stop":
                grades_str = input("Podaj 3 oceny oddzielone spacjami: ")
                add_student_output = add_student(database, name, grades_str)
                print(add_student_output["msg"]) # optional: add_student_output["msg", "name", "grades"]
        case 2:
            name = input("Podaj imię ucznia do wyświetlenia średniej ocen: ")
            avg_student_output = avg_student(database, name)
            print(f"Średnia ocen ucznia {name}: {avg_student_output}")
        case 3:
            best_student_output = best_student(database)
            print(f"Najlepszy uczeń to {best_student_output[0]} ze średnią {best_student_output[1]}")


while running:
    menu(database)