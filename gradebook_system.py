import heapq

while True:
    # introduction to program
    print("Welcome to the student gradebook system!")
    print("This gradebook systems allows you to input grades for a list of students as well as calculate the average of each students grades.\n")
    print("At the end of the calculation, there is a student ranking system that rank each student on their grade performance.")
    # input variables
    teacher = input("Please enter your name (The faculty member): ")
    academic_course = input("What academic course are teaching? ")
    list_of_students = input("Please display your list of students for the term:\n")
    # function call to detect a list of students
    # for each word, input a "," between each
    # ensure each letter at the beginning of each name is capitalized
    def detect_list_of_students(student_input):
        words = student_input.replace(",", "").split()
        capitalized = [w for w in words if w and w[0].isupper()]
        return len(capitalized) >= 2
    # detect students which do not have capitalized letters in the name
    # apply simple notice to upper case the letter their name
    while not detect_list_of_students(list_of_students):
        print("Please enter at least two capitalized student names.")
        list_of_students = input("Re-enter student list:\n")
    # print statements for displaying faculty name and students list
    print("\nFaculty: ", teacher)
    print("\nAcademic Course: ", academic_course)
    print("Students list: ", list_of_students)

    students = [name.strip() for name in list_of_students.replace(",", "").split()]

    gradebook = {student: [] for student in students}
    # enter grade for each student until complete
    for student in students:
        print(f"\nEntering grades for {student}")
        while True:
            grade = input("Enter a grade (or type 'done'): ")

            if grade.lower() == "done":
                break
            elif grade.isdigit() and 0 <= int(grade) <= 100:
                gradebook[student].append(int(grade))
            else:
                print("Invalid grade. Enter a number 0–100 or 'done'.")

    print("\n--- Final Grade Report ---")
    for name, grades in gradebook.items():
        if grades:
            avg = sum(grades) / len(grades)
            print(f"{name}: Grades = {grades} | Average = {avg:.2f}")
        else:
            print(f"{name}: No grades entered.")

    ranking = []
    for name, grades in gradebook.items():
        if grades:
            avg = sum(grades) / len(grades)
            heapq.heappush(ranking, (-avg, name))

    print("\n--- Student Ranking ---")
    for avg, name in sorted(ranking):
        print(f"{name}: {-avg:.2f}")

    # saves first developed gradebook into a txt file
    with open("gradebook.txt", "a") as file:
        file.write(f"faculty: {teacher}\n")
        file.write(f"Academic Course: {academic_course}\n")
        file.write("Students and Grades:\n")

        for name, grades in gradebook.items():
            if grades:
                avg = sum(grades) / len(grades)
                file.write(f"{name}: {grades} | Average = {avg:.2f}\n")

            else:
                file.write(f"{name}: No grades entered.\n")
        file.write("\nStudent Ranking: \n")
        for avg, name in sorted(ranking):
            file.write(f"{name}: {-avg:.2f}\n")
        print("grades submitted have been saved as gradebook.txt for viewing.")

    again =  input("Would you like to submit grades for another group of students? (yes/no)")
    if again != "yes":
        print("goodbye!")
        break
