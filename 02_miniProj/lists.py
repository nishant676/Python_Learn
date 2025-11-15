tea_varities = ["black", "Green", "White", "Oolong", "Orange"]
print(tea_varities) #o/p:-['blac', 'Green', 'White', 'Oolong', 'Orange']

#Particular print
print(tea_varities[2]) #o/p:-White
print(tea_varities[2:]) #o/p:-['White', 'Oolong', 'Orange']
print(tea_varities[1:1]) #o/p:- []

tea_varities[1:1] =["test", "test"] 
print(tea_varities) #o/p:-['blac', 'test', 'test', 'Green', 'White', 'Oolong', 'Orange']

print(tea_varities[1:2]) #o/p:['test']

# using loop print values

for teas in tea_varities:
    print(teas) # by default new line print with every value

for teas in tea_varities:
    print(teas, end="-") #o/p:black-test-test-Green-White-Oolong-Orange


if "black" in tea_varities:
    print("I have it")


# add new value in lists 
# => added in the last 
# => using append

tea_varities.append("Ginger") 

if "Ginger" in tea_varities:
    print("I have it already")


# pop:-
# => remove last value from list
print(tea_varities) # o/p:- ['black', 'test', 'test', 'Green', 'White', 'Oolong', 'Orange', 'Ginger']
print(tea_varities.pop()) # o/p:- Ginger

# Selected value delete
# => Use remove

tea_varities.remove("test")
print(tea_varities)

# insert value at selected position
tea_varities.insert(1, "Pink")
print(tea_varities) #o/p:['black', 'Pink', 'test', 'Green', 'White', 'Oolong', 'Orange']


# Copy values
coffe_menue = tea_varities.copy()
print(coffe_menue)


# print squares of nums till 10

squared_num = [x**2 for x in range(10)]
print(squared_num) #o/p:-[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cubed_num = [y**3 for y in range (5)]
print(cubed_num)# o/p:[0, 1, 8, 27, 64]