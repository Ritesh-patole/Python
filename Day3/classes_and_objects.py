class dog:
    def __init__(self, name, age):
         self.name = name
         self.age = age

    def bark(self):
        print("woff")

class Animal:
    def __init__(self, species):
        self.species= species

class cat(Animal):
    def meow(self):
        print("meow")

mydog = dog(name='tuffy', age='3')

print(f"My {mydog.name} is {mydog.age} old")

mydog.bark()

mycat = cat(species="Domestic")
print(f"This is a {mycat.species} cat.")
mycat.meow()




class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

person1=Person(name='Jake', age='32')
print(f"Hello, my name is {person1.name} and i am {person1.age} year old")

class employee:

    def __init__(self, name, sal):
        self.name=name
        self.sal=sal

    
    def defEmp(self):
        print("Name: ", self.name, " Salary: ", self.sal)

emp1=employee("Sam",1000)
emp1.defEmp()


string = "Python1"
def test(string):
    string="program"
    print("Inside function: ", string)
test(string)
print("Outside function:", string)


class Student:
    stream='CA'     #class var
    def __init__(self,name,roll):
        self.name=name      #instance var
        self.roll=roll

a = Student('jake', 2)

print(f"hi i am {a.name}, i am from {Student.stream} background and my roll number is {a.roll}")


class myclass:
    def smeth():
        print("This is static method")
    smeth = staticmethod(smeth)
    def cmeth(c1s):
        print("This is class method of ", c1s)
    cmeth= classmethod(cmeth)

myclass.smeth()
myclass.cmeth()


class myclass1:
    @staticmethod
    def smeth():
        print("2this is static method")
    @classmethod
    def cmeth(c1s):
        print("2this is class method of ", c1s)

myclass1.smeth()
myclass1.cmeth()
    



