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


#-------------------------------------------------
# Strip():-
# => used to remove unwanted spaces
chai = "  masala chai  "
print(chai) #o/p-->__masala chai__ <-indicating spaces 
print(chai.strip()) #-> o/p- masala chai  

#Replace(old value, new value):-
chaai = "lemon chai"
print(chaai.replace("lemon", "ginger")) #o/p--> ginger chai
print(chaai) # o/p --> lemon chai ==> original value is not changed here


# Split():-
tea = "lemon, Ginger, masala, mint"
print(tea.split()) #o/p-->['lemon,', 'Ginger,', 'masala,', 'mint']===> based on space segrigate

print(tea.split(", ")) #o/p-->['lemon', 'Ginger', 'masala', 'mint']===> based on comma and space seggrigate

# find():-
newChai = "Masala Chai"
print(newChai.find("Chai")) # o/p:- 7 ====>returning the index num
print(newChai.find("tea"))  # o/p:- -1 ===> means not present / not find 

# count():-

chaii = "Masala Chai Chai Chai Chai "
print(chaii.count("Chai")) #o/p:- 4 ==> total count of chai

# Formatter
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of  {} chai" #---> in {} we can palce values

print(order.format(quantity, chai_type)) #o/p:- I ordered 2 cups of  Masala chai

# Convert List to String using join():-

chai_variety = ["Lemon", "Masala", "Ginger", "Turmeric"]

print("".join(chai_variety)) #o/p:- LemonMasalaGingerTurmeric
print(" ".join(chai_variety))#o/p:-Lemon Masala Ginger Turmeric
print("-".join(chai_variety)) #o/p:- Lemon-Masala-Ginger-Turmeric
print(", ".join(chai_variety)) #o/p:- Lemon, Masala, Ginger, Turmeric

# Length:-
chai = "Masala Chaii"
print(len(chai)) #o./p:- 12

# Print every single letter

for letter in chai:
    print(letter) #o/p:- for every letter take one line by /n


# want to print double coat :-
# => use '\'
chai = "He said, \"Masala Chai is awsome\" "
print(chai) # o/p:-He said, "Masala Chai is awsome" 


# In String if  use double coat or slash and want it also display on printing time then use:-
# => use 'r'
new_chai = r"c:\useer\poc"
print(new_chai) #o/p:- c:\useer\poc

# Present or not (True or False)
chai = "Masala Tea"
print("Masala" in chai) #o/p:- True