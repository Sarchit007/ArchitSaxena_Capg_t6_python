'''
Class and object

class:-
->A class is a blueprint or template for creating objects.
It defines:
->Attributes (variables) → data
->Methods (functions) → behavior

Object:-
->An object is an instance of a class.
->It represents a real-world entity created using a class.

Constructor:
->In Python, a constructor is a special method that is automatically called when an object of a class is created. It is mainly used to initialize the object's attributes (variables).
->In Python, the constructor method is called __init__().

class method:
->In Python, a class method is a method that is bound to the class rather than the object.
->It works with the class itself, not with individual instances (objects).
->To create a class method, Python uses the @classmethod decorator.


static method:
->A static method in Python is a method that belongs to a class but does not use the class (cls) or object (self).
->It is defined using the @staticmethod decorator.
->Static methods are usually used for utility functions that are related to a class but do not need access to class or instance data.

'''

# class College:
#     c_name = "JU"
#     loc = "Jaipur"
   
#    Constructor Creation
    # def __init__(self,name,id,age):
    #     self.name=name 
    #     self.id=id
    #     self.age=age 


# s1 = College()   
# s1 = College("Archit",1,22)
# print(s1.name)


class Student:
    c_name="JU"
    loc="Jaipur"
    
    def __init__(self,name,id,age):
        self.name=name 
        self.id=id
        self.age=age 
   #object method
    def display(self):
        print(self.name)
        print(self.id)
        print(self.age)

#  creating class method
    @classmethod  
    def c_dis(cls):
        print(cls.c_name) 
        print(cls.loc)



# s1 = Student("Archit",1,22)      
# s2 = Student("ram",2,23)     
# s3 = Student("rahul",3,22)
# s4 = Student("ayush",4,23)
# s5 = Student("gopal",5,24)   

# s1.display()
# s2.display()
# s3.display()
# s4.display()
# s5.display()
# s1 = Student()
# s1.s_id = 2
# s1.s_name = "Ram"
# s1.s_age  = 23

# s2 = Student()
# s2.s_id = 3
# s2.s_name = "Ayush"
# s2.s_age = "24"

# print("Student 1")
# print(s1.s_id)
# print(s1.s_name)
# print(s1.s_age)

# print("Student 2")
# print(s2.s_id)
# print(s2.s_name)
# print(s2.s_age)

 

    