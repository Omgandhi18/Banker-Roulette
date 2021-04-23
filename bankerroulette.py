import random

names_string=input("Enter names Seperated by comma: ")
names=names_string.split(",")
length=len(names)
rand=random.randint(0,length-1)
person=names[rand]
print(person+" will pay the bill")
