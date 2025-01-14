#For loop for list
list = ["java","python","sql",".net"]
for i in list:
    print(i)

print("-------------------------------------------")

#For loop for str
str = "I love Python"
for i in str:
    print(i)

print("-------------------------------------------")

#For loop for list and Range function and else block
countrylist = ["India","UK","USA","UAE"]
for i in range(len(countrylist)):
    print(countrylist[i])
else:
    print("Country list is over")

print("-------------------------------------------")

#For loop for list and Range function[2] and else block
citylist= ["Bangalore","LA","Dubai","NY"]
for i in range(2):
    print(citylist[i])
else:
    print("City list is over")


print("-------------------------------------------")

#Nested for loop to print pattern

for i in range(1,5):
    for j in range(i):
        print(i, end="")
    print()
