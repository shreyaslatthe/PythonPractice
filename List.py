score = [10,20,76,102]
print(score)

print(score[0])
#print(score[4])
print(score[3])
print(score[-1])

#reverse List
print(score[::-1])
#Print range of values from list
print(score[0:2])


print(score + [1,2,3])
print(score + ["A","B","C"])

number = [1,2,3,4]
number[2]=90
print(number)
number.append(100)
print(number)

name=['a','b','c','d','e','f']
print(name)

name[2:5] = ['C','D','E']
print(name)

name[2:5] = []
print(name)

#length of List
print(len(name))

#Nested List
a = [1,2,3,4]
b = ['A','B','C']
x = [a,b]
print(x)
print(x[0])
print(x[1])

# Print the 2D value in nested list
print(x[0][2])
print(x[1][1])


