#Delete All Elements Based on User Decision
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

user = input("Clear list? type yes or no: ").lower()

if user == "yes":
    list1.clear()
    print(list1)

elif user == "no":
    print(list1)

else:
    print("Invalid Input")