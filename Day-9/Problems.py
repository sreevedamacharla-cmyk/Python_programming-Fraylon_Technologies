#47
string="    Python  "
# print(string[0]="j") raises a typeerror as strings are immutable i.e., they cant be modified or changed.


#48
word="Hello"
print("J"+word[1:])


#49
print(string.strip())
print(string.upper())


#50
first_name="Eugene"
last_name="Fitzerbut"
print(first_name+" "+last_name)


#51
print("-"*30)


#52
list1=["red","blue","green"]
print(",".join(list1))


#53
# using + in a loop is slow because each "+" creates an entire new string while .join() builds result in one efficient pass ,avoiding creating many new strings.


#54
fields=["name","age","city"]
csv_line=",".join(fields)
print(csv_line)



#55
msg="Py"
print(msg + "thon")


#56
score=90
print("Score: "+str(score))
print(f"Score: {score}")


#57
name="Asha"
age=25
print("Asha is 25")
print(name + " is " + str(age))
print(name,"is", age)
print(f"{name} is {age}")


#58
pi=3.141592
print(f"{pi:.1f}")


#59
num=100000000
print(f"{num:,}")


#60
x=7
print(f"{x:04d}")


#61
y=0.5
print(f"{y:0%}")


#62
s="hi"
print(f"{s:>10}")


#63
result="{0} {0}".format("hi")
print(result)


#64
name="asha"
age=25
result="%s is %d years old" %(name,age)
print(result)


#65
print("\thi \nHello")


#66
print(r"C:\Users")


#67
print("""Hello, My name is 'asha' and i am "25" years old""")


#68
# \\produces a single backslash
print("h\\e\\l\\l\\o")


#69
item="Apple"
qty=3
price=15.25
receipt_line=f"{item:<12}{qty:>4}{price:>8.2f}"
print(receipt_line)


#70
val1=-5
val2=5
print(f"{val1:+d}")
print(f"{val2:+d}")


#71
print(r"line1\nline2")


#72
val=3.14159
width=10
precision=2
result=f"{val:{width}.{precision}f}"
print(repr(result))



#Practice questions

#1
word="     Hello World!!            "
print(word.strip())


#2
colors=["teal","plum","Violet","wine"]
string="---".join(colors)
print(string)


#3
print(r"C:\users\Asha\Desktop")
print("C:\\users\\Asha\\Desktop")


#4
item2="Notebook"
qnty=5
price=150.54000
receipt=f"{item2:<12}{qnty:>4}{price:>8.2f}"
print(receipt)


#5
result="{0} {0}".format("Python")
print(result)