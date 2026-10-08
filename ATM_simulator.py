balance = 10000
pin = "1234"

print("===== ATM SIMULATOR =====")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Money deposited successfully!")
            print("New Balance:", balance)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient balance!")

        elif choice == "4":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")

else:
    print("Incorrect PIN!")
