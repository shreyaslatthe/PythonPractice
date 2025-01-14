#Keywords
def login(username,password):
    print(username,password)

login("test","pwd")
login(username= "test1", password= "pwd2") #Keyword usage

#Args
def getMarks(*arg):
    for x in arg:
        print(x)
getMarks(10,15,20,40)
getMarks("A","A+","B+","C","D")

#Key Value Args
def getStudentMarks(**args):
    for key, value in args.items():
        print("%s = %s" %(key,value))
getStudentMarks(t1=10, t2=20, t3=30)


#Lambda functions :: Annonymous function
#Function without any name

cube = lambda x: x*x*x
print(cube(4))

total = lambda marks: marks/6
print(total(400))

