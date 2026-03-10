'''
Inheritance
-Inheritance means a child class gets the properties and methods of a parent class.
-It helps in reusing code so we don’t need to write the same code again.
here
Parent → base class
Child → derived class (inherits from Parent)

Type of Inheritance:
Single Inheritance:
-One child class inherits from one parent class.

Multiple Inheritance
-One child class inherits from more than one parent class.

Multilevel Inheritance
-A class inherits from another child class.

Hierarchical Inheritance
-Multiple child classes inherit from one parent class.

Property Method
The @property decorator is used to access a method like an attribute.

Polymorphism:
Polymorphism means:
-Same operation behaves differently depending on context.


File_Handling:
-File handling is used to create, read, write, append, and manage files in Python.

-File is a type of container in which we contain or store some data.
by using extension name, we can identify what type of data is there inside of it
ex:- .txt, .py, .html ,,,,etc
Before handling any file, taking permission is very much important,

open():
open('filename.ext'/'absolute_path',mode)

close():
var_name.close()

there are 3 different modes are present

write(w)
read(r)
append(a)
Write mode:

only write (w)
write + read (w+)
write binary (wb)
write & read binary (wb+)
Read mode:

only read (r)
read + write (r+)
read binary (rb)
read & write binary (rb+)
Append mode:

only append (a)
append + read (a+)
append binary (ab)
append & read binary (ab+)
For write operations:

in this , if the file is not present, it will create one then perform write operation.
if the file is already present, them it will override the pre data with the new one.
write(str_data): Single line of data
writelines([lin11,line2.....]) : multiple line of data
For wirte Operations:

read(): Display whole file in normal format
readline(): Reads only one line from the file.
readlines(): Reads all lines and returns them as list.

CSV_File:
csv = comman seperated value
CSV operations or methods
csv.reader() --> Reads CSV file rows as list data
csv.writer() --> Creates writer object to write CSV data
writer.writerow() --> Writes one row of data into CSV
writer.writerows() --> Writes multiple rows of data into CSV
csv.DictReader() -->Reads CSV rows as dictionary using headers
csv.DictWriter() --> Writes dictionary data into CSV with headers

Pickle & JSON:
Json operations or method
dumps(): Encryption
loads(): Decryption
1. Json,  
2. pickle,


'''


# class Animal:
#     def speak(self):
#         print("Animal makes a sound")


# class Dog(Animal):
#     def bark(self):
#         super().speak()
#         print("Dog barks")


# d = Dog()
# d.speak()


# class Emp:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# class Manager(Emp):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)   
#         self.department = department

#     def display(self):
#         print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


# m = Manager("Archit", 500000, "IT")
# m.display()   



# class Student:
#     def __init__(self, marks):
#         self._marks = marks

#     @property
#     def marks(self):
#         return self._marks


# s = Student(85)
# print(s.marks)



# class Circle:
    
#     def __init__(self, radius=0):
#         self.radius = radius

#     def inp(self):       
#         self.radius = int(input("Enter the radius: "))

#     def area(self):        
#         return 3.14 * self.radius ** 2

#     def surface(self):      
#         return 2 * 3.14 * self.radius



# c = Circle()
# c.inp()
# print(c.area())
# print(c.surface())


# file = open("temp.txt","w+")
# file.write("i am the first line!")
# file.seek(0)
# print(file.read())
# file.write("i am the first line!")
# file.writelines([
#     "first line\n",
#     "sec line\n",
#     "third line\n"
# ])
# file.close() 

# import csv
# from datetime import date

# file = open('expense.csv', 'a+', newline='')
# w = csv.writer(file)
# file.seek(0)
# r = csv.reader(file)
# print(list(r))

# w.writerow(['Date', 'Category', 'Amount'])
# w.writerows(
#     [
#         [date.today(), 'Travel', 2000],
#         [date.today(), 'chai', 400],
#         [date.today(), 'panner', 4000]
#     ]
# )

# file.close()



import json
file = open('temp2.txt', 'a+')

# data = {
#     'full_name' : 'Aditya',
#     'user_id' : 123456,
#     'password' : '**'
# }

print(f"Original Data: {data}")
print(f"Type of original data: {type(data)}")
print()

enc_data = json.dumps(data)

# file.write(enc_data)

file.seek(0)
print(file.read())


# print("Encrypted Data:", enc_data)
# print("Type of Encrypted data:", type(enc_data))
# print()

# dec_data = json.loads(enc_data)

# print("Decrypted Data:", dec_data)
# print("Type of Decrypted data:", type(dec_data))
file.close()