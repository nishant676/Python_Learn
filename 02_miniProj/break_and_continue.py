Hero = ["batMan", "Superman", "robin", "joker", "flash"]

for legend in Hero:
    if legend == "joker":
        continue
    print(legend) #--->o/p==>batMan Superman robin flash

for SuperHero in Hero:
    if SuperHero == "robin":
        break;
    print(SuperHero) #--->o/p==>batMan Superman


# Tuple:

marks = (15, 28, 65, 45, 28,28,28)
print(marks.count(28))


# Set

sports = {"cricket", "basket ball", "Tennis", "carrom"}
for sport in sports:
    print(sport)


# Dictionary

Heros = {"Flash" :"DC", "Strange":"Marvel" }
print(Heros["Strange"])
# Add new value

Heros["Ben10"] = "Cartoon"

print(Heros)