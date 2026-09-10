students = {}

while True:
    print("\n===== ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")

        students[roll] = {
            "name": name,
            "present": 0,
            "total": 0
        }

        print("Student added.")

    elif choice == "2":
        roll = input("Enter roll number: ")

        if roll in students:
            status = input("Present or Absent (P/A): ").upper()

            students[roll]["total"] += 1

            if status == "P":
                students[roll]["present"] += 1
                print("Attendance marked Present.")
            else:
                print("Attendance marked Absent.")
        else:
            print("Student not found.")

    elif choice == "3":
        for roll, student in students.items():
            total = student["total"]

            percentage = (
                student["present"] / total * 100
                if total > 0 else 0
            )

            print(
                roll,
                student["name"],
                "-",
                f"{percentage:.2f}%"
            )

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
