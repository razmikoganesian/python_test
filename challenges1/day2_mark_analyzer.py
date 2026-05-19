
def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name:  ").strip()

        if name.lower() == "done":
            break
        if name in students:
            print("Student already exist")
            continue

        try:
            marks = float(input(f"Enter marks for {name}:  "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks")

    return students

def display_report(students):
    if not students:
        print("No student data")
        return
    
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks) / len(marks)

    topper = [name for name, score in students.items() if score == max_score]
    lower = [name for name, score in students.items() if score == min_score]

    print("\n students marks report ")
    print("--" * 30)
    print(f"Total students: {len(students)} ")
    print(f"Average marks for students: {average:.2f} ")
    print(f"Highest marks for students: {max_score} by {','.join(topper)} ")
    print(f"Lowest marks for students: {min_score} by {','.join(lower)} ")

    print("-" * 30)
    print("Detailed Marks ")
    for name, scores in students.items():
        print(f"- {name} : {scores}")

students = collect_student_data()
display_report(students)


    
