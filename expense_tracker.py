from datetime import datetime

#I am using list to store all data i.e. in dictionary format
main_list =[]

#this function is adding input data into a dictionary then adding the dictionary in our main list
def add_expense(date, category, description, amount):
    expense_item = {"date":date,"category":category,"description":description,"amount":amount}
    main_list.append(expense_item)
    print("\nExpense added successfully!")

#this function is responsible for showing all expenses 
def view_expense():
    print("\n Expenses -->")
    if len(main_list) != 0:
        for i in main_list:
            print(i)
    else:
        print("There is no expense available in list.")

def mainfunc():
    while True:
        print("\nChoose an option to move forward->\n")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            date = datetime.now().strftime("%d/%m/%y")
            category = input("\nEnter category: ")
            description = input("\nEnter description: ")
            amount = float(input("\nEnter amount: "))
            add_expense(date, category, description, amount)

        elif choice == 2:
            view_expense()

        elif choice == 3:
            print("Thank you")
            break

        else:
            print("\nInvalid Choice!")

mainfunc()