a = int(input("Enter an integer: "))
if a % 2 != 0: #when reminder is not equal to 0
    fact = 1
    for i in range(2, a + 1):
        fact *= i
        a_digits = len(str(fact))#to find lenght in the form of string
    print("Factorial:", fact)
    print("Number of digits in factorial:", a_digits)
else:
    a_str = str(a)
    if a_str == a_str[::-1]:#reversing a string
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
