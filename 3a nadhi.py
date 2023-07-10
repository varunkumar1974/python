a = input("Enter a list of numbers separated by commas: ").split(",")
a = [int(num) for num in a]

c = int(input("Enter the element to be found: "))

positive_indices = []
negative_indices = []

for i in range(len(a)):
    if a[i] == c:
        positive_indices.append(i + 1) 
        negative_indices.append(-(len(a) - i ))
        
o = len(positive_indices)
print(f"Element {c} occurs {o} time(s) in the list.")
print("Positive Index :", ", ".join(str(index) for index in positive_indices))
print("Negative Index :", ", ".join(str(index) for index in negative_indices))
