#function without arguments
def test():
    print("Hello World")
test()

#function with 1 argument
def sum(a):
    print(a+10)
sum(20)

#function with 2 argument and return
def add(x,y):
    return x+y
z = add(4,5)
print(z)

#function with optional/default parameter
def myCountryName(name="India"):
    print(name)
myCountryName()       #Default parameter
myCountryName("USA")  #optional parameter

#pass list in function
def test1(list):
    for i in list:
        print(i)

name = ["java", "python", "SQL", "Ruby"]
test1(name)

def CapitalName(CountryName):
    if CountryName == "India":
        return "Delhi"
    elif CountryName == "USA":
        return "Washington DC"

print(CapitalName("India"))
print(CapitalName("USA"))

#Function calling itself (Recursive function)
def fact(num):
    if (num>1):
        num = num * fact(num-1)
    return num
print(fact(5))


