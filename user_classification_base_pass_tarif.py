user_category=input('Enter user category: ').lower()

if user_category == "student":
    sub_category=input('Enter subcategory: ').lower()
    if sub_category == "undergraduate":
        print(f"your Monthly Base Fee is : ₹500")
    elif sub_category == "postgraduate":
        print("Your Monthly Base Fee is : ₹350")
    else:
        print("You have enter wrong subcategory")
elif user_category == "staff" or "faculty":
    sub_category=input("Enter subcategory: ")
    if sub_category == "resident faculty":
        print('Your Base Fee is : ₹800')
    elif sub_category == "visiting" or 'guest faculty':
        print("Your Base Fee is : ₹1200")
    else:
         print("You Have enter wrong subcategory")
else:
    print("you have enter wrong user category")