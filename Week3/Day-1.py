#1
nums=[10,20,30,40,50]
print(nums[-2])


#2
print(nums[1:4])


#3
marks=[82,92,78,65,90,89,69,41]
print(marks[::-1])


#4
marks.sort()
print(marks)


#5
grid=[[0]*2]*2
grid[0][0]=5
print(grid)


#6
marks.append(20)
print(marks)


#7
marks.insert(1,100)
print(marks)


#8
nums.extend([50,60])
print(nums)


#9
nums+=[70]
print(nums)


#10
print(nums.index(50))


#11
nums[0]=99
print(nums)


#12
nums.remove(99)
print(nums)


#13
x=marks.pop(0)
print(marks)


#14
del nums[4]
print(nums)


#15
nums.clear()
print(nums)
7

#16
print(len(marks))

#17
lst=[]
for i in range(1,6):
    lst.append(i)
print(lst)


#18
alph=["a","b","c","d"]
alph[2]="x"
print(alph)



#19
alph.remove("x")
print(alph)


#20
fruits=["Cherry","Litchi","Strawberry"]
print("Cherry" in fruits)


#21
pets=["Dog","Cat","Rabbit","Duck"]
print(pets.index("Duck"))


#22
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,116,17,18,19,20]
print(num[::2])


#23
print(pets[::-1])


#24
list1=[1,2,3,4]
copy=list1[:]
print(copy)
print(copy is list1)  #Returns false ass the copy of the list occupies a new memory space than list1.


#25
print(list1[20:30]) #Returns an empty list


