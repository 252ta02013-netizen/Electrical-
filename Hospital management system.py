patients = []

def add_patient():
    patient_id = input("Patient ID: ")
    name = input("Patient Name: ")
    age = int(input("Age: "))
    disease = input("Disease: ")

    patients.append({
        "id": patient_id,
        "name": name,
        "age": age,
        "disease": disease
    })

    print("Patient added successfully.")


def view_patients():
    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print("\nPatient ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Disease:", patient["disease"])


while True:
    print("\n===== HOSPITAL MANAGEMENT =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
