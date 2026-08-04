#21
name="Sreeveda"
age=20
city="Hyderabad"
print("Hello! I am",name," \nI am ",age,"years old"," \nand I'm from",city)

#22
print("4", "8", "2026",sep="-")



#23
print("loading", end="")
print("....", end="")
print("Done")



#24
date=3
month=8
year=2026
print(date,month,year, sep="-")



#25
print("Address:\nabc street\nHyderabad, Telangana")


#26
name="Sreeveda"
score=85
print(name,score, sep="\t")
#or 
print(name,"\t",score)


#27
print("C:\\Users\\abc\\OneDrive\\Desktop")


#28
print("This is a sentence\"using double quotes\"")


#29
print(f"{name} is {age} years old.")



#30
print(name,"is",age,"years old.")



#31
print(name + " is", str(age) + " years old.")


#32
# print("Age:" +25)  #fails because python is a strongly typed language and cannot concatenate string datatype with an number

print("Age:",str(25))
print("Age:25")
print(f"Age:{25}")



#33
pi=3.14159265
print(f"{pi:.2f}")



#34
num1=12500000
print(f"{num1:,}")



#35
num2=0.256
print(f"{num1:.1%}")



#36
print("Message1")
print()
print("Message2")
#or
print("Message1 \n\nMessage2")



#37
print('a','b',sep='', end='!')
print('c')


#38
print("***\n***\n***")


#39
print("Inline Comment")  #This line prints Inline Comment in the output



#40
#comment line 1
#comment line 2
#comment line 3


#41
'''This is a multi-line comment'''

#42
# print("This is a line of code")


#43
def greet(name):
    """Greets the user for the given name"""
    return f"Hello, {name}!"

print(greet.__doc__)
help(greet)


#44
def add(a,b):
    """Adds a with b and returns the sum"""
    return(a+b)
print(add.__doc__)


#45
#A comment is ignored by python, it is mainly for user understanding
#A docstring is stored  by python and can be read via help() or __doc__


#46
#x+=1 #increment
#x+=1 #Skip the header row



#47

#1.Declare age
age=20
#2.How old will they be next year?
next_year_age=age+1
#3.Print next_year_age
print(next_year_age)



#48
# Python doesnot have a special multi lne comment because the inventor guido van rossum wanted python to be a simple and clean language.
# multi line comments can be written usng # on each line or """ or '''



#Practice questions

#1
print("python" ,"is", "fun", sep="*")

#2
print("Python", end=" ")
print("Programming")

#3
item="Laptop"
price=80000
print(f"{item} costs {price:,}")

#4
print("item","\t","price")
print(item,"\t",price)

#5
savings=18500.672
print(f"{savings:.2f}")

#6
print("A", "B", sep="---", end="!")
print("C", "D", sep="---")


#7
score=0.852
print("Result:",f"{score:.1%}","Done!", sep=" | ")
