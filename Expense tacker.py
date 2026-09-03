print("Welcome TO Expense Tracker")

balance=int(input("Enter Your balance: "))
expense=0

print("Enter i for income or e for expense")
change_type=input()
print("you said:",change_type)
print("please Say How Much")
taka=int(input())
print("you entered:",taka);
if change_type == "e":
    balance=balance-taka
    print("your new balance:", balance ,"taka")
elif (change_type=="i"):
    balance=balance+taka
    print("your new balache:", balance, "taka")
else:
    print("vulval type korcho")

print("Thank You For Visiting Us ")

