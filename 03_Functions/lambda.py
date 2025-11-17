cube = lambda x: x ** 3

print(cube(3))  
print("--------------------------------")


# Args
def sum_all(*args):

    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8))

# Kwargs
# => print in a key value pair

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_kwargs(name="superman" , power="fly")
print_kwargs(name="superman" )
print_kwargs(name="superman" , power="fly")
print_kwargs(name="superman" , power="fly", enemy= "Dr. Shakal")