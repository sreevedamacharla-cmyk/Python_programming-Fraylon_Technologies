#1
my_dictionary={} 
print(my_dictionary)  #Empty dictionary



#2
dict1={"name":"Asha",
"age":21,
"student":True,
}
print(dict1)


#3
student=dict(name="Alexa",Branch="CSE",Score=85)
print(student["name"])



#4
pairs=dict([("a",10),("b",20),("c",30)])
print(pairs)



#5
new=dict(zip(["xyz","pqr","abc"],[12,23,34]))
print(new)



#6
student["Gender"]="Female"
print(student)


#7
student.update({"name":"Alex","Gender":"Male"})
print(student)



#8
print(student.pop("Score"))
del student["Branch"]
print(student)



#9
student.clear()
print(student)




#10
for k in pairs:
    print(k)
for v in pairs.values():
    print(v)
for k,v in pairs.items():
    print(k,"-->",v)




#11
print(list(pairs.keys()))
print(sum(pairs.values()))
print(max(pairs, key=pairs.get))



#12
squares={x:x*x for x in range(5)}
print(squares)



#13
inverted={v:k for k,v in pairs.items()}
print(inverted)



#14
filtered={k:v for k,v in squares.items() if v%2==0}
print(filtered)



#15
from_two={k:v for k,v in zip("abcdef",[1,2,3,4,5,6])}
print(from_two)
