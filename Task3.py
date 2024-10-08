#Remove an Element by Index or Value
list1 = ["Ac","Rea","Nhia","Bobby"]
num = [1,2,3,4,5,]
print("Initial list:", list1)
print("Initial list:", num)

wow = input("Remove or Pop?: ").lower()

if wow == "remove":
    user1 = input("Who to Remove? ")
    list1.remove(user1)

elif wow == "pop":
    user2 = int(input("Number to Remove? "))
    num.pop(user2)

print("Updated list:", list1)
print("Updated list:", num)