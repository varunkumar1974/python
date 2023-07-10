a = input("Enter the first string: ")
b = input("Enter the second string: ")

i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        i += 1
        j += 1
    else:
        i += 1

if j == len(b):
    print("YES")
else:
    print("NO")
