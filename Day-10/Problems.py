#73
word="   Python"
print(repr(word.strip()))


#74
word2="Hello World"
print(word2.upper())
print(word2.lower())


#75
text="The quick brown fox"
print(text.title())


#76
word3="python Programming"
print(word3.capitalize())


#77
word4="Banana"
print(word4.count("a"))


#78
print(word4.find("na"))


#79
print(word4.startswith("Ban"))
print(word4.endswith("na"))


#80
# both find() and index() are used to find the index of a substring but find() returns -1 if the substring is not found whereas index() raises an error.


#81
date="2026-08-12"
print(date.split("-"))


#82
string="a,b,c,,d,e"
print(string.split(","))
# split() method keeps the empty values


#83
string2="a b"
print(string2.split())
# if no argument is given for split() it splits at whitespaces.


#84
date2=["2026","08","12"]
result="-".join(date2)
print(result)


#85
print(word2.replace("l","L"))


#86
print(word2.replace("l","L",1))


#87
print("42".isdigit())


#88
text2="abcdef123456"
print(text2.isalnum())


#89
a="9"
print(a.zfill(4))


#90
print("Hi".ljust(6,"-"))


#91
print("Hi".center(8,"."))


#92
word5="xxxxxhixxxx"
print(word5.strip("x"))


#93
print(isinstance(True,int))


#94
print(True+True+False)


#95
print(0<78<100)


#96
# Falsy values in python are 
# 0 #int
# 0.0 #float
# 0j #complex
# "" #empty string
# [] #empty list
# {} #empty dictionary
# () #empty tuple
# set() #empty set
# None
# False


#97
print(bool("False"))
#Here false is the value of a string, as long as the string is not empty ,bool treats it as a truthy value.


#98
print(type(5==5)) # implies true , so returns  bool 


#99
values=[3,-1,0,"None","x"]
#Truthy values are 3,-1 and x
 

#100
print(0<=10<=100)


#Practice questions

#1
print(word2.swapcase())

#2
print(word3.find("a"))

#3
new_word="abc"
print(new_word.isdigit())
print(new_word.isalpha())


#4
new_text="    "
print(new_text.isspace())


#5
new_word2="PYTHON PROGRAMMING"
print(new_word2.isupper())
print(new_word2.islower())




