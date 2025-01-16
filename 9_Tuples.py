#Tuples
'''
a tuple is an immutable, ordered collection of items.
Tuples are used to store multiple items in a single variable and are similar to lists,
but with one key difference: they cannot be modified after creation.
Tuples are commonly used to group related data and ensure the data remains unchanged.

Key Features of Tuples:
1. Ordered: Tuples maintain the order of items.
2. Immutable: Once created, you cannot modify, add, or remove items from a tuple.
3. Allow Duplicates: Tuples can have duplicate elements.
4. Heterogeneous: They can store items of different data types (e.g., integers, strings, etc.).
'''

names = ("tom","dick","Harry","Ram")
marks = (35,60,98,87)
employeeData = ("Tom",25,'M',80.2,True)
print(employeeData)
print(employeeData[2])
print(employeeData[3])
print(employeeData[1])
#print(employeeData[5]) #Index out of Range
print(employeeData[-1])
print(employeeData[-5])
print(employeeData[::-1]) #Reverse Tuple

l = [1,2,3,4]
l[2] = 100 # List data can be changed with index as ref
print(l)

'''
t = (1,2,3,4)
t[2] = 100
print(t) #'tuple' object does not support item assignment '''

#Concatenation of tuples
t1 = (1,2,3,4)
t2 = (3,4,5)
print(t1+t2)

#Range slicing Tuple
t11 = (1,2,3,4,5,6,7,8,9)
print(t11[2:6])

#In operator
employeeData1 = ("Tom",25,'M',80.2,True)
print (25 in employeeData1)
print ("F" in employeeData1)

#Not in
print (79.2 not in employeeData1)

#Length
print (len(employeeData1))

#Max / Min
t22 = (91,82,103,34,85,26,97,38,9)
print(max(t22))
print(min(t22))