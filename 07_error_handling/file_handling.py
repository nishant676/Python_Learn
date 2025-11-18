file = open('youtube.txt', 'w')

#--> menas open this file in which mode 
#  'w' ===> write mode  ||   'r' ====> read mode only
# here 'w' used , if that file is not present means it automatically create this file, so we have to used try catch block

try:
    file.write('chai with nishant')
finally:
    file.close()

# Easy Another way to do same thing as upper we wrote 

with open('youtube.txt', 'w') as file :
    file.write('chai with nishant')