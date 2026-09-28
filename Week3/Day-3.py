#1
set1={1,2,3,4,5}
print(set1)


#2
print(type({})) #dictionary



#3
vowels={"a","e","i","o","u"}
print("i" in vowels)


#4
empty=set()
print(empty)



#5
set1.add(7)
set1.add(5)   #duplicates are ignored
print(set1)


#6
set1.remove(1) #raises an error is 1 is not present in the set
set1.discard(2) #does not raise an error even if the set does not contain the number. 
print(set1)


#7
set2={9,8,7,7,8,4,5,1,2,1}
z=set2.pop() #removes a random value in a set
print(set2)


#8
set2.clear()
print(set2)# returns set() which denotes an empty set


#9
a={1,2,3,4,5,5}
b={2,5,6,7,8,9}
print(a|b)
print(a&b)
print(a-b)
print(a^b)


#10
string="consistency"
count=0
for char in string:
    if char in vowels:
        count+=1

print(count)


