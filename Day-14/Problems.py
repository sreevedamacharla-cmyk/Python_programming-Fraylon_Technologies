#1
tup=()
print(type(tup))



#2
single_tup=("Apple") #str 
print(type(single_tup))


#3
new_tup="23","34"
print(new_tup)
print(type(new_tup))


#4
char_tup=tuple("PYTHON")
print(char_tup)


#5
tupl=(0,)*5
print(tupl)


#6
nums=(12,23,34,45,56,67)
print(nums[1],nums[-1])


#7
print(nums[::-1])


#8
points=(12,25,69)
x,y,z=points
print(x)
print(y)
print(z)


#9
scores=(24,56,12,99,89,69,75,45,33,9)
print(min(scores))
print(max(scores))


#10
print(sum(scores))
print(len(scores))


#11
digits=(0,[1],2,3,4,5)
# digits[2]=9  #tuple doesnot support item assignment as it is immutable#


#12
digits[1].append(9)
print(digits)



#13
one=(1)         #not a tuple
two=(2,)        # is a tuple



#14
from collections import namedtuple
user=namedtuple("User",["name","age"])
u=user("Asha",20)
print(u.name)
print(u.age)


#15
nums2=(1,3,2,3,5,7,3,0,8,90,3)
print(nums2.count(3))


