# # #1
# # num=int(input("Enter a number: "))
# # if num%3==0:
# #     print("FIZZ")
# # elif num%5==0:
# #     print("BUZZ")
# # elif num%15==0:
# #     print("FIZZBUZZ")
# # else:
# #     print("invalid")



# # #2
# # val=-9
# # if val>0:
# #     print("Positive")
# # elif val<0:
# #     print("Negative")
# # else:
# #     print("Zero")



# # #3
# # year=2024
# # if year%4==0 or year%400==0 and year%100!=0:
# #     print("LEAP YEAR")
# # else:
# #     print("NOT A LEAP YEAR")



# # #4
# # num1=20
# # num2=30
# # num3=40
# # if num1>num2 and num1>num3:
# #     print(num1,"is greatest")
# # elif num2>num1 and num2>num3:
# #     print(num1,"is greatest")
# # elif num3>num1 and num3>num2:
# #     print(num1,"is greatest")



# # #5
# # marks=int(input("Enter marks: "))
# # if marks<=100 and marks>=90:
# #     print("GRADE-A")
# # elif marks<90 and marks>=80:
# #     print("GRADE-B")
# # elif marks<=80 and marks>=70:
# #     print("GRADE-C")
# # elif marks<70 and marks>=60:
# #     print("GRADE-D")
# # elif marks<60 and marks>=50:
# #     print("GRADE-E+")
# # elif marks<50 and marks>=40:
# #     print("GRADE-E")
# # else:
# #     print("FAIL")



# # #6
# # number=90
# # result="Even" if number%2==0 else "Odd"
# # print(result)


# # #7
# # vowels=["a","e","i","o","u"]
# # char="i"
# # if char in vowels:
# #     print("Vowel")
# # else:
# #     print("Consonant")



# # #8
# # side1=9
# # side2=7
# # side3=9
# # if side1==side2==side3:
# #     print("Equvilateral triangle")
# # elif(side1==side2!=side3) or (side2==side3!=side1) or (side3==side1!=side2):
# #     print("Isoscales triangle")
# # else:
# #     print("Scalene triangle")



# # #9
# # x=3
# # y=18
# # if x>0 and y>0:
# #     print("Quadrant 1")
# # elif x>0 and y<0:
# #     print("Quadrant 4")
# # elif x<0 and y>0:
# #     print("Quadrant 2")
# # elif x<0 and y<0:
# #     print("Quadrant 3")
# # else:
# #     print("Origin")




# # #10
# # a=10
# # b=5
# # operator=input("Enter an operator[=,-,/,*,%]: ")
# # if operator=="+":
# #     print(a+b)
# # elif operator=="-":
# #     print(a-b)
# # elif operator=="/" and b!=0:
# #     print(a/b)
# # elif operator=="*":
# #     print(a*b)
# # elif operator=="%":
# #     print(a%b)
# # else:
# #     print("Invalid operator")




# # #11
# # age=21
# # if age<15:
# #     print("Ticket price: 50")
# # elif age>15 and age<=50:
# #     print("Ticket price: 100")
# # else:
# #     print("Free")



# # #12
# # password=input("Enter password: ")
# # upper=False
# # lower=False
# # digit=False
# # special=False
# # for ch in password:
# #     if ch.isupper():
# #         upper=True
# #     elif ch.islower():
# #         lower=True
# #     elif ch.isdigit():
# #         digit=True
# #     else:
# #         special=True

# # if len(password)>8 and upper and lower and digit and special:
# #     print("VALID PASSWORD")
# # else:
# #     print("!!!INVALID PASSWORD!!!\nPassword must contain atleast 8 characters including uppercase, lowercase,digits and a special character")

    


# # #13
# # import random
# # choices=["rock","paper","scissors"]
# # user=input("Enter your choice[rock, paper, scissors]: ")
# # bot=random.choice(choices)
# # print("Bot chose: ",bot)
# # if user=="paper" and bot=="rock":
# #     print("you win!")
# # elif user=="scisscors" and bot=="paper":
# #     print("you win!")
# # elif user=="scisscors" and bot=="rock":
# #     print("you win!")
# # elif bot==user:
# #     print("Its a tie!")
# # else:
# #     print("Bot won")



# # #14
# # a=1
# # b=4
# # c=2
# # d=b**2-4*a*c
# # if d>0:
# #     print("real roots")
# # elif d==0:
# #     print("equal real roots")
# # else:
# #     print("complex rooots")



# # #15
# # units=int(input("Enter units consumed(range 0 to 400): "))
# # bill=0
# # if units<=100:
# #     bill=units*1
# # elif units<=200 and units>100:
# #     bill= (100*1)+((units-100)*2)
# # elif units<=300 and units>200:
# #     bill= (100*1)+(100*2)+((units-200)*3)
# # else:
# #     bill=(100*1)+(100*2)+(100*3)+((units-300)*4)
# # print(" Your Bill is: ",bill)



# # #16
# # status=int(input("Enter the status code: "))
# # match status:
# #     case code if 200<=code<300:
# #         print("Success")
# #     case code if 400<=code<500:
# #         print("Client error")
# #     case code if 500<=code<600:
# #         print("Srever error")
# #     case _:
# #         print("Unknown error")



# # #17
# # day=input("what day is today? ")
# # match day:
# #     case "saturday" | "sunday":
# #         print("Weekend")
# #     case _:
# #         print("Weekday")




# # #18
# # x=10
# # y=2
# # operator=input("Enter an operator[+,-,*,/,%]: ")
# # match operator:
# #     case "+":
# #         print(x+y)
# #     case "-":
# #         print(x-y)
# #     case "*":
# #         print(x*y)
# #     case "/":
# #         print(x/y)
# #     case "%":
# #         print(x%y)
# #     case _:
# #         print("Invalid operator")




# # #19
# # shape=tuple(input("Enter shape and dimensions: ").split(","))
# # match shape:
# #     case ("circle",r):
# #         area=3.14*float(r)**2
# #         print("Area: ",area)
# #     case ("rectangle", l, w):
# #         area=float(l)*float(w)
# #         print("Area: ",area)
# #     case ("triangle",b,h):
# #         area=0.5*float(b)*float(h)
# #         print("Area: ",area)
# #     case _:
# #         print("Invalid shape")


# # #20
# # def parse_command(command):
# #     match command:
# #         case {"action":"move", "direction":direction}:
# #             print(f"Moving {direction}")
# #         case {"action":"stop"}:
# #             print("Stopping")
# #         case _:
# #             print("Invalid")

# # parse_command({"action":"move", "direction":"north"})

# # #21
# # light=input("Enter the current state of light[red,yellow,green]: ")
# # match light:
# #     case "red":
# #         print("Next state is Yellow")
# #     case "yellow":
# #         print("Next state is Green")
# #     case "green":
# #         print("Next state is Red")
# #     case _:
# #         print("Invalid")




# # #22
# # vowels=["a","e","i","o","u"]
# # vowels_upper=["A","E","I","O","U"]
# # char=input("Enter any character: ")
# # match char:
# #     case char if char in vowels or char in vowels_upper:
# #         print("Vowel")
# #     case char if char.isalpha() and (char not in vowels and char not in vowels_upper):
# #         print("Consonant")
# #     case char if char.isdigit():
# #         print("Digit")
# #     case _:
# #         print("Symbol")




# # #23
# # def grade_band(grade):
# #     match grade.upper():
# #         case "A"|"A+":
# #             print("Excellent")
# #         case "B"|"B+":
# #             print("Good")
# #         case "C"|"C+":
# #             print("Average")
# #         case "D"|"D+":
# #             print("Can do better")
# #         case "E"|"E+":
# #             print("Poor")
# #         case "F":
# #             print("Fail")
# #         case _:
# #             print("Invalid grade")

# # grade_band("B")
        



# # #24
# # def exp_eval(op,a,b):
# #     match op:
# #         case "+":
# #             print(a+b)
# #         case "-":
# #             print(a-b)
# #         case "*":
# #             print(a*b)
# #         case "/":
# #             print(a/b)
# #         case "%":
# #             print(a%b)
# #         case _:
# #             print("Invalid operator")

# # exp_eval("-",5,10)



# #25
# def menu_option(choice):
#     match choice:
#         case 1 | "1":
#             print("Navigating to profile")
#         case 2 | "2":
#             print("Opening dashboard")
#         case 3 | "3":
#             print("Adding item to cart")
#         case 4 | "4":
#             print("Pay and Buy")
#         case _:
#             print("Invalid")
# menu_option(3)



#26
n=1234
total=0
while n>0:
    total+=n%10
    n//=10
print("Sum of digits: ", total)


#27
n=1234
rev=0
while n>0:
    digit = n%10
    rev=(rev*10)+digit
    n//=10
print(rev)