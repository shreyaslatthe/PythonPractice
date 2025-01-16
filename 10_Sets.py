'''
In Python, a set is an unordered, mutable collection of unique elements.
Sets are commonly used to store items where duplicates are not allowed and
to perform mathematical set operations such as union, intersection, and difference.
Key Features of Sets:
1. Unordered: The elements in a set have no specific order, and their order may change.
2. Unique Elements: A set automatically removes duplicate elements.
3. Mutable: Sets can be modified by adding or removing elements.
4. Heterogeneous: Sets can store elements of different data types.
'''

s1 = {100, "tom", 25, 'M', 80.2, True}
s2 = {1,2,3,2,1,2,4}
print(s2)

#set function
s3 = set("python")
print(s3)

s4 = set([30,40,30,20,40,50])
print(s4)

s5 = set((10,20,30,45))
print(s5)

#While creating set object, you can store only numbers, strings, float & tuple
#List & dictionary cannot be stored in set

#set operations; union: |
p1 = {1,2,3,4,5}
p2 = {4,5,6,7,8}
print(p1|p2)

#Intersection : &
print(p1&p2)

#difference of sets : -
print(p1 - p2)
print(p2 - p1)

#Symmateric difference of sets : ^
print(p1 ^ p2)

#add
s1 = {"java","python","C++"}
s1.add("VBA")
print(s1)

#update
s1.update(["sql","ruby"])
print(s1)

s1.update(("html","css"))
print(s1)

#Clear
s1.clear()
print(s1)

#copy
lang = {"java","python","C++"}
lang1 = lang.copy()
print(lang1)

#discard
st={"tom","dick","harry"}
st.discard("tom")
print(st)
st.discard("ram")
print(st)

#remove
st1={"tom","dick","harry"}
st1.remove("dick")
print(st1)
st1.remove("ram")
print(st1) #Throws error.


