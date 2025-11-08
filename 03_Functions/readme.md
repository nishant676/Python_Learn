# Math
=> we have Math pkg we can use that by writting
**import math** . u can also see all the methods using  **print(dir(math))**
=> to use specific method from math pkg
e.g:
**square root**
from  math import sqrt
print(sqrt(6))

=> If u want all the function then use *
from math import *


## User Defined Function
=> def----> defination

e.g: def print_sum(first, second):
          print(first + second)
   
 print(2,3) -----------> function call
 => if supoose did not provide second value and u want it will take default value if there were no value 
    e.g::  def print_sum(first, second=4):-----> it'll take 4
          print(first + second)
