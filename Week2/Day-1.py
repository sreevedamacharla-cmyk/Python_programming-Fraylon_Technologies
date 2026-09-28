#1
value=2_500_000
print(value)


#2
print(float(0b1111))
print(bin(15))


#3
value=200
print(bin(value))
print(oct(value))
print(hex(value))


#4
print(round(4.5))  #4
print(round(5.5))  #6


#5
print(round(3.141592,3))


#6
print(round(2500,-3))


#7
print(0.1+0.2)
#(0.1+0.2)!=0.3 as the computer stored floating point numbers as binary numbers.This is known as binary float imprecision.


#8
a=0.2
b=0.1
print(abs(a-b)<1e-9)


#9
print(divmod(29,4))
#divmod() returns both quotient and remainder at the same time. divmod(29,4) returns (7,1) where 7 is the quotient and 1 is the remainder.


#10
print(max([4,9,1,7]))
print(min([4,9,1,7]))


#11
print(abs(-8-5))


#12
print(sum(range(1,101)))


#13
print(int(9.99))
#when 9.99 is converted to int using int() it truncates the decimal part so returns 9.


#14
print(int(-9.99)) 
#truncates towards zero


#15
print(int("17"))


#16
#print(int("17.0")) returns an error as the value is both string and float. To make it work , we have to convert the d]string to float first and then convert into int.


#17
print(int(float("17.0")))


#18
print(int(True))
print(int(False))


#19
print(int("101",2))


#20
print(int("ff",16))


#21
print(float(7))
print(str(7))


#22
print(str([1,2,3]))


#23
print(bool(0))  #False
print(bool("")) #False
print(bool("0"))    #True
print(bool(1))  #True


#24
try:
    age=int(input("Enter your age: "))
except ValueError:
    print("!! Enter a whole number !!")



#25
print(int(-7.9))
print(-7.9//1)
#floor devision always rounds down the value while int() does not.


#26
print(int(3.99999999))
print(round(3.99999999))








