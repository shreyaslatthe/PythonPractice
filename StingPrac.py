s1="Hello World"
s2="test selenium"

print(s1)
print(s2)

print(s1[0])
#print(s1[13]) // Index out of range error
print(s1+" "+s2)

#New line & Tab
print("Hello \n World")
print("test \t selenium")
print("test "*5)
print(s1[0:5])

#IN operator
print("test" in s1)
print("test" in s2)
print("Hello" not in s1)

#formatting operator
print("My name is %s and my age is %d" %("Shrey", 31))

s3= ''' Test selenium
and
this is python code'''
print(s3)

s4= """ Test2 selenium
and
this is python code2"""
print(s4)

#how to handle string literals
print('Hi I\'m Shrey')
print("Hi my fav pgm lang is \"python\" and Iam loving it")

#String functions
str="this is python code"
print(str.capitalize()) #The first letter is changed to upper case

str1=("This is Python Code And I Love Python")
print(str1.count("Python")) #Count is used to count the number of occerance

print(str1.find("Code")) #Provides the index value of the str in find
print(str1.find("test")) #If str is not present then returns -1 as value

print(len(str)) #Provides the length of the str
print(str1.lower()) #Prints the str in lower case

str4="bsdba"
print(max(str4)) #Prints max alphabet value in the str
print(min(str4)) #Prints least alphabet value in the str

str5="Hello test python"
print(str5.replace("Hello","Bye")) #Replaces the keywords in the str

str6="java Hello python Hello"
print(str6.split("Hello"))

st = "Python is best"
print(st[-1])
print(st[0])
print(st[::-1])
print(len(st))
a="test python"
b="test python"

print(a is b)
print(a == b)