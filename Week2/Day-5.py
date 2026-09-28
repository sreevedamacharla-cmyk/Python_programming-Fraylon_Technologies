#101
print(17//5)
print(17%5)


#102
x=20
x+=10
print(x)
x//=3
print(x)


#103
a=10
b=15
print(a if a>b else b)


#104
number=20
print("Even" if number%2==0 else "Odd")


#105
num=10
sign="Positive" if number>0 else "Negative" if number<0 else "Zero"
print(sign)



#106
num=-50
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")



#107
# When the problem's solution requires multi-step logis or is complex to be handled by ternary, we use if-else block



#108
print(2**8)
#** is used for exponentiation i.e., here 2**8 means 2 to the power of 8.


#109
print(7==7.0)
#checks value equality across types.


#110
print(5!=5)


#111
val=67
print(1<=val and val<=100)


#112
print(1<=val<=100)


#113
print(0 and 5)
print(3 and 5)


#114
print(""or "default")


#115
print("Hi" or "x")


#116
name=""
print(name or "Guest")


#117
print(not(5>3))


#118
name=True
admin=True
print(name and admin)


#119
a=[2,5]
b=[2,5]
c=a 
print(a is b)
print(a is c)


#120
#is None is preferred over ==None as it i correct and a unique singleton.


#121
lst1=[1,2,3,5,6,7]
print(5 in lst1)


#122
word="Hello"
print("z" not in word)


#123
print(6&3)
#6 is 0110 and 3 is 0011 , when both are computed ,it returns 0010 which is 2.



#124
print(6|3)
#6 is 0110 and 3 is 0011 , when both are computed ,it returns 0111 which is 7.


#125
print(6^3)


#126
print(4<<2)
print(16==4*2^2)


#127
print(20>>2)
print((5==20/2)^2)


#128
# butwise $ logical and operation to each corresponding pair of bits of two integers while logical and evaluates expressions from left to right using short=circuit evaluation.



#129
text="Programming"
print("gram" in text)


#130
a=b
print(a is b)


#Practice Questions
#1
marks=76
print("Pass" if 40<=marks<=100 else "Fail")


#2
year=2026
print("Leap year" if year%4==0 else "Not a Leap year")


#3
year2=2024
if year2 % 4 == 0:
    print(year2," is a Leap year")
else:
    print(year2,"is not a Leap year")



#4
age=19
if age<18:
    print("Minor")
elif age>=18 and age<=30:
    print("Adult")
elif age>31 and age<=59:
    print("Middle age")
else:
    print("Senior citizen")


#5
is_student=True
senior_citizen=True
print("Eligible for discount" if is_student and senior_citizen else "No discount")


#6
score=85
if 0<=score<40:
    print("Fail")
elif 40<=score<=60:
    print("Grade: C")
elif 60<score<=80:
    print("Grade: B")
elif 80<score<=90:
    print("Grade: A")
else:
    print("A+")


#7
side1=10
side2=10
side3=10
if side1==side2==side3:
    print("Equilateral Triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("Iscoscales Triangle")
elif side1!= side2!=side3:
    print("Scalene Triangle")
else:
    print("Not a Triangle")



#8
num2=45
if num2%3==0 and num2%5==0:
    print("Given number is divisible by both 3 and 5")
elif num%3==0 and num%5!=0:
    print("Given number is divisible by only 3")
elif num%3!=0 and num%5==0:
    print("Given number is divisible by only 5")
else:
    print("Not divisible")



#9
vowels=["a","e","i","o","u"]
word="u"
if word in vowels:
    print("Is a vowel")
else:
    print("Not a vowel")




#10
a=10
b=20
print(a if a>b else b)


#11
num3=45
print("Positive" if num3>0 else "Negative" if num3<0  else "Zero")



#12
print(13 and 0)
print(0 and 5)


#13
print(0 or 5)
print(10 or 0)