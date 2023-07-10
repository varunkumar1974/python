a= int(input("Enter number of elements in list: "))
b= []

for i in range(a):
    num = int(input("Enter the value: "))
    b.append(num)

c= True

for i in range(len(b) - 1):
    if b[i] > b[i + 1]:
        c = False
        break

if c:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
