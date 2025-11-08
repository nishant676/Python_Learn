first = input("Enter first Number :")
operator = input("enter operation u want to perform(+, -, /, *, %)")
second = input("Enter second Number:")

first = int(first)
second = int(second)
if operator == '+':
    print(first + second)
elif  operator == '-':
    print(first - second)    
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print("Invalid Operator")
