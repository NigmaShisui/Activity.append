#Sort and Reverse a Mixed List
list1 = ['1',"Ac",'2',"Nhia", '3',"Bobby"]
print(list1)

user = input("Sort Alphabetically or Sort Reverse? type sort or reverse: ").lower()

if user == "sort":
    list1.sort()
    print(list1)

elif user == "reverse":
    list1.reverse()
    print(list1)