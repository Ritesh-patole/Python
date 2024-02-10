class Animal:
    def eat(self):
        print("Eating")
class dog(Animal):
    def bark(self): 
        print("Barking")

d = dog()
d.eat()
d.bark()







class stud:
    def getdata(self, rollno, name, course):
        self.rollno=rollno
        self.name=name
        self.course = course
    
    def displaystud(self):
        print("Rollno: ", self.rollno)
        print("Name:", self.name)
        print("Course :", self.course)

#inheristance
class test(stud):
    def getmarks(self, marks):
        self.marks=marks
    def displaymark(self):
        print("total marks:", self.marks)

r = int(input("Enter roll no: "))
n = input("Enter name: ")
c = input("Enter course name: ")
m = int(input("Enter marks: "))

print("Result: ")
studl=test()
studl.getdata(r,n,c)
studl.getmarks(m)
studl.displaystud()
studl.displaymark()






# Single Inheritance 
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Multiple Inheritance
class A:
    def method_A(self):
        print("Method A")

class B:
    def method_B(self):
        print("Method B")

class C(A, B):  # Multiple inheritance
    def method_C(self):
        print("Method C")

# Multilevel Inheritance
class X:
    def method_X(self):
        print("Method X")

class Y(X):
    def method_Y(self):
        print("Method Y")

class Z(Y):
    def method_Z(self):
        print("Method Z")

# Hierarchical Inheritance
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Objects and usage
my_dog = Dog()
my_dog.speak()  # Accessing method from the superclass
my_dog.bark()   # Accessing method from the subclass

my_instance = C()
my_instance.method_A()
my_instance.method_B()
my_instance.method_C()

my_z = Z()
my_z.method_X()
my_z.method_Y()
my_z.method_Z()

my_cat = Cat()
my_cat.speak()  # Accessing method from the common superclass
my_cat.meow()   # Accessing method from the subclass

