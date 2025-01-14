a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

if (a>b and a>c and a>d):
    print("The Largest number is a:",a)
elif (b>c and b>d):
    print("The Largest number is b:", b)
elif (c>d):
    print("The Largest number is b:", b)
else:
    print("The Largest number is c:", d)