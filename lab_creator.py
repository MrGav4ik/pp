import os

lab_number = input("Enter lab number (e.g. 04): ")
task_number = int(input("Enter number of tasks (e.g. 6): "))
student_id = int(input("Enter your student id: "))
surname = input("Enter your surname: ")
name = input("Enter your name: ")

directory_name = f"Lab{lab_number}"

if os.path.isdir(directory_name) == False:
    os.mkdir(directory_name)

    for i in range(1, task_number + 1):
        with open(f"Lab{lab_number}/Lab{lab_number}_Zad0{i}_{surname}.py", "w") as f:
            f.write(
f"""# Laboratorium: {lab_number}; Zadanie 0{i}; Autor: {surname} {name} nr albumu {student_id}
# Oświadczam, że zadanie wykonałem samodzielnie.
""")
else:
    print("Directory already exists")
