#27
word="Consistency"
print(word[0],word[-1])


#28
word2="Programming"
print(word2[4])


#29
print(word[:4])


#30
print(word[-3:])


#31
print(word2[:-2])


#32
print(word2[2:8])


#33
print(word[::2])


#34
string="Python"
print(string[::-1])

#35
print(word==word[::-1])


#36
print(string[0:20])
# This does not give an error because python only slicec the string upto its length.


#37
string2="Program"
print(string2[2:5])


#38
mail="user@email.com"
print(mail[mail.find("@")+1:])


#39
alphabet="abcdefghijklmnopqrstuvwxyz"
print(alphabet[::3])


#40
print(alphabet[:5][::-1]+alphabet[5:])


#41
file_ext="report.pdf"
print(file_ext[file_ext.find(".")+1:])


#42
print(word[-10:-2])


#43
print(string[:len(string)//2], string[len(string)//2:])


#44
print(string[100:200])  #returns blank space (empty)


#45
print(word[::2])


#46
print(word[1:-1])


#Practice problems
#1
print(word[-3:])


#2
print(string[::-1])


#3
print(string[0],string[-1])


#4
s="hello"
# print(s[10])  # raises an error "string indexing out of range" as 10th index is not present in the word.


#5
print(string[0:len(string)])


#6
print(word[:-2])


#7
text=input("Enter a word to check Palindrome: ")
if text==text[::-1]:
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")


#8
print(word2[::-2])


#9
print(word[3:])


#10
digits="0123456789"
print(digits[::2])


#11
print(word[0:10:2])
