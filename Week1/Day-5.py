#123
my_list=[1,3,5,7,9,11]
print(my_list[0])


#124
my_tuple=(23.01,85,91.1,43,12,6)
# my_tuple[2]=67


#125
my_set={23,45,67,89,90,12,67}
print(my_set)



#126
my_dict={
    "name":"asha",
    "age":25,
}
print(my_dict["name"])



#127
# Type                 ordered?                  Changable?                   Duplicates?                      Syntax
# list                   yes                       yes                           yes                             []
# tuple                  yes                       no                            yes                             ()
# set                    no                        yes                           no                              {}
# dict                   yes                       yes                         no(keys)                         {k:v}


#128
print(type({}))
print(type(set()))


#129
print(type(my_list))
print(type(my_set))
print(type(my_tuple))
print(type(my_dict))


#130
name="Asha"
print(type(name)==int)


#131
print(isinstance(name, int))


#132
print(isinstance(my_tuple, int))


#133
#isinstance is preferred over type() because it reads clearly and also accepts tuple of types to check several at once


#134
my_dict["student"]=True
print(my_dict)


#135
val1="42"
print(int(val1))


#136
print(float("3.14"))


#137
print(str(100))


#138
print(int(3.9))
#int() chops off the decimal part but does not round it.


#139
print(float(7))


#140
print(bool(0))  #False
print(bool("")) #False
print(bool("0"))    #True
print(bool(1))  #True


#141
print(list("abcde"))


#142
print(tuple(my_list))
print(set(my_list))


#143
#print(int("3.5"))
#to parse this we have to convert "3.5" into float first
print(int(float("3.5")))



#144
# print(int("abc"))
# int() only accepts strings that look like whole numbers.



#145
print(5+2.0)


#146
print(True+1)
# in boolean True means 1 and false means 0, boolean is int subtype.


#147
# "5"+3 fails beacuse 5 is a string and implicit conversion wont mix strings and numbers


#148
print(int("5")+3)


#149
print("5"+str(3))


#150
name=input("Enter your name: ")
print("Hello", name)


#151
age=int(input("Enter your age: "))
age+=1
print(age)


#152
num1=int(input("Enteer number 1: "))
num2=int(input("Enteer number 2: "))
print("Sum: ",num1+num2)


#153
print(round(3.9))
print(int(3.9))
#int(3.9) returns 3 as it truncates the decimal 
#round(3.9) returns 4 as it rounds off the number


#154
my_list=list(my_set)
my_list.sort()
print(my_list)


#155
print(4/2)#float 2.0
print(int(4/2))#int 2

#156
age=int(input("Enter your age: "))
age*=12
print("Your age in months is:",age)


#Practice questions

#1
fruits=["litchi","mango","guava"]
print(fruits[0])

#2
marks=(24,98,67,55,59,90,24)
# marks[0]=47  #TypeError
print(marks)

#3
student={
    "name":"asha",
    "age":21,
    "group":"Computer Science",
    "score":85.5,
}
print(student)
print(student["score"])

#4
text="Python.."
print(list(text))

#5
student["Grade"]="A"
print(student)

#6
val2=10.5
print(isinstance(val2,float))
print(isinstance(val2,str))

#7
age=int(input("Enter your age: "))
age+=1
print(f"Next year you will be {age} years old.")

#8
list2=[3,89,76,90,223,12,9,0,56]
list2.sort(reverse=True)
print(list2)

#9
tup1=(5,2,8,2,1)
set1=set(tup1)
print(set1)
print(list(set1))


#10
tup2=("red", "green", "blue")
print(tup2[-2])

#11
print(len(set1))

#12
set1.add(67)
print(set1)



