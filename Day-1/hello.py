#6
name="Sreeveda"
city="Hyderabad"
print("Hello! I am",name,"and I'm from",city)



#10
#Before
a=1; b=2; c=3
#after
a=1
b=2
c=3



#11
#explicit---using \
print(10+20+\
30+40)
#implicit---using ()
print(10+20+
30+40)



#12
if 10>5:
    print("5 is greater than 10")
    print("Hence, the condition is true")
print("This is the line outside the block")



#13
#buggy code
# if 10>5:
# print("10 is greater than 5")--- raises and indentation error

#fixed code
if 10>5:
    print("10 is greater than 5")



#14
#buggy code
# if 10>2:
#   print("10 is greater than 2")--- raises and indentation error because of only 2 spaces instead of 4

#fixed code
if 10>2:
    print("10 is greater than 2")


#15
age=30
Age=35
print(age)
print(Age)



#17
my_list=[1,2,3,
4,5,6,
10
]
print(my_list)


#20
a=1
b=5
if a>b:
    print("A")
print("B")



#Practice questions
#1
cat="milo"
cat="sugar"
print(cat)



#2
number=8
if number>5:
    print("Message 1")
    print("Message 2")

print("Message 3")



#3

val1=50
print(val1+20) 
print(type(val1))#int

val2="20"
print(val2+"20") 
print(type(val2)) #str