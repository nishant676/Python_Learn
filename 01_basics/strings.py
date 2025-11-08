name= "Chrish Hemsworth"

print(name.upper())
print(name.lower())

print(name.find('h'))

print(name.replace("Chrish", "thor"))
print('Chris' in name)

# Arithmatic Operations
print(5+2)
print(5*10)
print(5/2) # here it gives 2.5 but if u want to tale only before decimal

print(5//2) # ans== 2

print(4 ** 2) # 4 to power 2 --> 16


# IF-Else

age = 2

if age>=18:
    print("You can vote")
    print("cause u r an adult")
elif age < 18 and age > 3:
    print("You cant vote")
    print("You are teenager")
else :
    print("you are a baby")