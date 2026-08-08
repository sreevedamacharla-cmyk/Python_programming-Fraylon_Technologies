#157
name="Asha"
course="Computer Science"
year=4
print(f"My name is {name}\nI am a {course} student\nI'm in my {year}th year.")


#158
print("1","2","3", sep=" | ")


#159
name="Asha"
age=25
print(name,"is", age)
print(name+" is "+str(age))
print(f"{name} is {age}")


#160
a,b=5,10
print(a,b)
a,b=b,a 
print(a,b)

#161
p=q=r=0
print(p,q,r)


#162
# 1value=15--invalid (Cannot start with a number)
# 1 value=15--invalid (cannot have spaces)
# value@1=15--invalid (no special characters are allowed except _)
# value1=15--valid
# value_1=15--valid
# new_value=15--valid


#163
year="2026"
new_year=int("2026")
new_year+=1
print(f"{new_year}")


#164
print(17//5)# returns the integer result of quotient after division
print(17%5)# returns the remainder after division


#165
num=48
print("Number :",num)
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")


word="apple"
if "a" in "apple":
    print("True")
else:
    print("False")



#166
pi=3.14159265
print(f"{pi:.3f}")


#167
num2=int(input("Enter a number: "))
print("Double of the number is: ",num2*2)


#168
text="Total:"
value=500
print(text+ str(500))
print(f"{text} {value}")


#169
name="Sreeveda"
print(name.upper())
print(name)


#170
values=[True,False,True,True]
print("Number of Trues are:",sum(values))


#171
count=1
def increment_count():
    global count 
    count+=1
    print(count)

increment_count()
print(count)


#172
word2="Programming"
print(word2[3:7])


#173
my_list=[1,2,1,4,3,3]
print(set(my_list))
new_list=sorted(my_list)
print(new_list)


#174
num3=10
num4=2
print(num3/num4)
print(type(num3/num4))
print(int(num3/num4))


#175
print("Item\tQty\tPrice")
print("Laptop\t1\t50,000")


#176
print(0.1+0.2)
#the computer stores the floating numbers as binary(binary float representation)

#177
def sum(a,b):
    """Returns the sum of two numbers"""
    return(a+b)

print(sum.__doc__)
print(sum(10,50))


#178
capitals={
    "Telangana":"Hyderabad",
    "India":"New Delhi",
     "West bengal":"Kolkata",
    
}

print(capitals["India"])


#179
val1=20
val2=30
print(val1+val2)
print(val1*val2)


#180
num5=2.675
print(f"{num5:.2f}")


#181
print(True+True+False)


#182
# "for" is not a legal variable name as it is a built-in python keyword and as per naming rules for any variable we should not use python's built-in keywords.


#183
print(int(3.99))
print(round(3.99))


#184
str1="""This
is a 
multi-line
string"""
print(str1)


#185
bill=int(input("Enter the bill: "))
tip=bill*0.15
print(f"Tip: {tip:.2f}")


#186
name="Asha"
age=25
city="Hyderabad"
student=True
print(f"Name: {name} Age: {age} City: {city} Student: {student}")



