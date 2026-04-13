#Simple banking application.
#User input to show balance, Withdrew money , deposit money.
balance = 0
kyc_documents = {}

def check_balance():
    pass
    print(f"Your current balance is {balance}")
    print("==========================================")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print(f"You can not deposit a negative amount")
        print("==========================================")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("You can not withdraw a negative amount")
        print("==========================================")
    elif amount > balance:
        print("You can not withdraw a negative amount/"
              "Or an amount exceeds your balance")
        print("==========================================")
    else:
        balance -= amount

def update_kyc(new_docs):
    global kyc_documents
    kyc_documents.update(new_docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

        print("==========================================")


if __name__ =="__main__":
    print("==========================================")
    print("!! Welcome to Sir, Sam's bank !!")
    print("==========================================")

    while True:
        print("1. Check Balance: - ")
        print("2. Deposit an amount:  - ")
        print("3. Withdraw an amount: - ")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit: -")
        choice = input("Please enter your choice: 1-6")
        print("==========================================")
        if choice == "1":
            check_balance()

        elif choice == "2":
            amt = float(input("Please enter the amount to deposit: "))
            deposit(amt)
            print(f"Amount {amt} deposit successfully.")

        elif choice == "3":
            amt = float(input("Please enter the amount to withdraw: "))
            withdraw(amt)
            print(f"Amount {amt} withdraw successfully.")

        elif choice == "4":
            check_kyc()

        elif choice == "5":
            try:
                n_documents = int(input("How many documents would you like to add? "))
                temp_docs = {}
                for i in range(n_documents):
                    key = input(f"Enter document {i + 1} type (e.g., Passport): ")
                    value = input(f"Enter {key} number: ")
                    temp_docs[key] = value
                update_kyc(temp_docs)
                print("KYC updated successfully.")
            except ValueError:
                print("Invalid input. Please enter a number for the count.")
        elif choice == "6":
            break
        else:
            print("Invalid input,Please enter a valid input: !!!! ")
            print("================================================")
    print("Thank you for using Sir, Sam's bank !")


