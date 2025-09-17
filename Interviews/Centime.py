s = 'PPPPRRAAAAPPR'
result = ""

count =1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count +=1

    else:
        result+=str(count) + s[i-1]
        count =1


#Add the last character group
result +=str(count) + s[-1]

print(result)

#class
class Employee:
    #class variable to track number of objects
    _count=0
    _max = 3 #maximum allowed objects

    def __init__(self,name,emp_id):
        if Employee._count>=Employee._max:
            raise Exception(f"Cannot create more than {Employee._max} Employee objects!")

        self.name= name
        self.id = emp_id
        Employee._count+=1 #increase counter when object is created
#Testing
e1 = Employee("chandra1",10)
e2 = Employee("chandra2",20)
e3 = Employee("chandra3",30)

print("3 objects created successfully")

#This will raise error
e4 = Employee("chandra",40)