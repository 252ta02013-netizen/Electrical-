balance = 0

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Amount withdrawn successfully.")

    elif choice == "3":
        print("Current Balance:", balance)

    elif choice == "4":
        print("Thank you for using our bank.")
        break

    else:
        print("Invalid choice.")
