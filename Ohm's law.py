print("===== OHM'S LAW CALCULATOR =====")
print("Formula: V = I × R")

print("\nWhat do you want to calculate?")
print("1. Voltage (V)")
print("2. Current (I)")
print("3. Resistance (R)")

choice = int(input("Enter your choice: "))

if choice == 1:
    current = float(input("Enter current (I) in Amperes: "))
    resistance = float(input("Enter resistance (R) in Ohms: "))

    voltage = current * resistance
    print(f"\nVoltage = {voltage:.2f} V")

elif choice == 2:
    voltage = float(input("Enter voltage (V) in Volts: "))
    resistance = float(input("Enter resistance (R) in Ohms: "))

    if resistance == 0:
        print("Resistance cannot be zero.")
    else:
        current = voltage / resistance
        print(f"\nCurrent = {current:.2f} A")

elif choice == 3:
    voltage = float(input("Enter voltage (V) in Volts: "))
    current = float(input("Enter current (I) in Amperes: "))

    if current == 0:
        print("Current cannot be zero.")
    else:
        resistance = voltage / current
        print(f"\nResistance = {resistance:.2f} Ω")

else:
    print("Invalid choice!")
