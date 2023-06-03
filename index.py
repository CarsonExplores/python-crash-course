# Module 5 Challenge

print("================================================")
print("                 Grocery List")
print("================================================")
print("1) View Grocery List")
print("2) Remover Groceries")
print("")
print("Enter an option number and press ENTER: ")
option = input()

if option == "1":
    groceries = ["Carrots", "Apples", "Cookies", "Sandwich Meat"]
    print(groceries)
else:
    option == "2"
    print("Enter in the grocery item and press ENTER:")
    user_input = input()
    groceries = ["Carrots", "Apples", "Cookies", "Sandwich Meat"]
    groceries.remove(user_input)
    print(groceries)
