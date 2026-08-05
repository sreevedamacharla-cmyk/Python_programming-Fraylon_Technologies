#49
num=0
num+=4  #step1
num+=6  #step2
print(num)


#50
num-=4
print(num)


#51
num*=2
print(num)


#52
name="Py"
name+="thon"
print(name)


#53
x=10
x//=3
print(x)


#54
y=10
y%=4
print(y)


#55
z=2
z**=4
print(z)


#56
count=0
count+=1
print(count)


#57
count=0
mylist=[10,20,30]
for items in mylist:
    count+=items
print(count)


#58
c=1
c+=5
print(x)
# x has to be declared 1st becaause pyhton reads the old value and then imlements any operation, without any initial value ot wont be able to perform the required operation


#59
name="Sreeveda"
age=20
marks=8.53
student=True
print(type(name),"\n",type(age),"\n",type(marks),"\n",type(student))


#60
# "=" is used for assignment as it binds a name to a value i.e., stores a value in itself so it cannot be used for equality

#61
x=5
y=x
x=10
print(x,y)


#62
var=5
print(type(var))
var="5"
print(type(var))
var=[5]
print(type(var))


#63
# Variable naming rules
# -Must start with a letter or underscore 
# -cannot start with a digit
# -may contain letters,digits and underscores
# -cannot contain spaces or any other special characters like @,-,+ etc
# -cannot be a reserved python keyword


#64
# var=1--valid
# Var1=1--valid
# Var_1=1--valid
# var@1=1--invalid
# 1var=1--invalid
# var 1=1--invalid
# new var=2--invalid
# 2 new@var=2--invalid
# new_var=3--valid


#65
# 2score=1 fails because a variable's name cannot start with a number
# but score2 can work as it meets the requirements of a variable name


#66
# class is a reserved key word in python. user cannot use python's key words as variables as they already have a definition


#67
#badly named
# p=25
# usrnm="asha"
# MAXNUMBEROFATTEMPPTS=3

# refactored into clean snake case
person_age=25
user_name="asha"
max_login_attempts=3



#68
MAX_LOGIN_ATTEMPTS=3


#69
# Python key words that cannot be used a variable names are:
# if,class,true,for,while


#70
age=10
Age=15
AGE=20
print(age,"\n",Age,"\n",AGE)


#71
# Naming Conventions:
# -snake_case : used for variables and functions
# -UPPER_CASE : used for constants(variables that don't change)
# -PascalCase : used for class names
# -_leading_underscore : used for internal use (private)


#72
_internal=7246018252
print(_internal)


#73
x,y,z=1,2,3


#74
a=b=c=0


#75
x,y=y,x
print(x,y)


#76
lst=[5,10]
a,b=lst
print(a)
print(b)


#77
fruits=["mango","litchi","guava"]
a,b,c=fruits
print(a)
print(b)
print(c)


#78

#a,b=1,2,3  #Too many values to unpack


#79
name,age="asha",28
print(name)
print(age)


#80
a=25
print(a)


#81
print(a,b,c)


#82
val1=800
val2=3.14159265
print("The values are",f"{val1:.,}, {val2:.2f}")


#83
first_name="John"
last_name="Doe"
print(first_name +last_name)


#84
age=25
print("Age:"+str(age))


#85
# "Score" + 90 doesnot work because a string and integer cannot be concatenated



#86
name="Asha"
age=25
city="Hyderabad"
is_student=True
print(f"Name: {name} | Age: {age} | City: {city} | Student: {is_student}")


#87
length=5
width=8
area=length*width
print(f"Area : {area:.1f}")


#88
a,b,c=1,2,3
a,b,c=c,b,a
print(a,b,c)


#89
x,y,z,w=5,6,7,8
x,y=w,z
print(w,x,y,z)



#90
x=y=10
x=20
print(x,y)



#Practice questions

#1
movie="Inception"
rating=8.8
is_favorite=True
print(f"{movie} has a rating of {rating}. Favorite: {is_favorite}")


#2
colors=["Teal", "Magenta","Aquamarine","Plum"]
print(colors[0])
print(len(colors))


#3
print("Shopping list:\n\t-Apples")


#4
total_minutes=198
hours=total_minutes//60
remaining_minutes=total_minutes%60
print(f"{hours} hours and {remaining_minutes} minutes")


#5
a=bool("")
b=True+True+False-True
c=int(4.5)
d=type(None)
print(a,b,c,d)
print(type(a),type(b),type(c),type(d))


#6
numbers=[35,85,42,91,98,71]
print(numbers[-1])
print(numbers[1:4])



#7
string="Python Programming"
new_string=string.lower()
print(new_string)


#8
print(string[ :10])
