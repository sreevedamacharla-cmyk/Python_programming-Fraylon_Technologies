#92
name="Asha"

def greet():
    print(f"Hello {name}")
greet()



#94
count=0
def increment_count():
    global count
    count+=1
print(f"Before function call {count}")
increment_count()
print(f"After function call {count}")


#97
def function():
    age=25
    print(age+1)
function()
# print(age)--returns nameerror


#99
var1=500
var2=3.14
var3 = 5+2j
print(type(var1))
print(type(var2))
print(type(var3))


#100
val=2730**90
print(val)  #no overflow


#101
print(f"{val:_}")


#102
num1=7
num2=2
print(num1/num2)  #3.5
print(num1//num2)  #3
print(num1%num2)  #1
print(num1**num2)  #49


#103
print(0.1+0.2==0.3)
print(0.1+0.2)
#binary floating point representation: computers store floating point numbers in binary but not in decimal


#104
number=int(input("Enter a number: "))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")



#105
num=2+3j
print(num.real)
print(num.imag)


#106
print("This is Karan's laptop")
print('This is Karan\'s laptop')


#107
print('''This is a
3 line
string''')



#108
string1="Python Programming is fun"
print(string1[0])
print(string1[-1])


#109
word="python"
print(word[0:3])



#110
print(len(string1))


#111
first_name="Guido"
middle_name=" Van"
last_name=" Rossum"
print(first_name+ middle_name+ last_name)

word2="hello!!!"
print(word2*3)


#112
print(string1.upper())
print(string1.lower())
text="  python programming      "
print(text.strip())


#113
text2="a,b,c,d"
print(text2.split(","))


#115
val1=5
val2=10
print(val1>val2)
print(val1<val2)
print(val1==val2)
print(val1!=val2)


#117
print(bool(0))  #False
print(bool("hi"))  #True
print(bool([]))  #False
print(bool(None))  #False


#118
flags=[True,False,False,False,True,True,True]
print(sum(flags))



#119
none_variable=None
print(none_variable is None)



#120
def hello():
    print("Hello!!")
print(hello())



#122
score1=97
score2=81
score3=93
sum1=score1+score3+score3
avg=sum1/3
print(f"The Average score is {avg:.2f}")




#practice questions

#1
string2="    PYTHON, Java, C++, java            "
print(string2.strip())


#2
passed=[True,False,False,True,True]
print(sum(passed))

#3
x=42
y=3.5
z="100"
print(type(int(z)))


#4
marks=20
def increase_marks():
    marks=40
    print("Inside function:", marks)

increase_marks()
print("Outside function:", marks)

