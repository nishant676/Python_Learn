import math
# Floor
a = math.floor(3.5)
print(a) # o/p--> 3 ===> will give u the closest value

b = math.floor(-4.5)
print(b) #o/p---> -5 

# Trunc----> take u toward near zer

c = math.trunc(2.8)
print(c) #o/p---> 2

d = math.trunc(-2.8)
print(d) #o/p---> -2

print(hex(65)) #o/p--> 0x41
print(bin(26)) #o/p--> 0b11010

print(int('10000',2))  #---o/p--> 16  (binary conversion)

#RANDOM Value :==>[randint , choice,  shuffle]
import random
val = random.randint(1,12) #---> give random value===> (starting , ending)
print(val) # o/p --. 7,6 etc

#Random Choice
l1 = ['lemon', 'masala', 'ginger', 'mint']
chooseOne = random.choice(l1)
print(chooseOne)

# Shuffle --> original one
uncertain = random.shuffle(l1)
print(l1)