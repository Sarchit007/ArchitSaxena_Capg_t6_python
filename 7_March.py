'''
Types of Arguments:
1.Positional Arguments
->Arguments are passed in the same order as the parameters in the function definition.

2.Keyword Arguments
->Arguments are passed using parameter names, so order doesn't matter.

3.Default Arguments
->A parameter has a default value if no argument is provided.

4.Variable-Length Arguments (*args)\
->Used when you don't know how many arguments will be passed.
'''
#positional argument
# def add(a, b):
#     return a + b
# print(add(5, 3))

# #keyword argument
# def student(name, age):
#     print(name, age)
# student(age=20, name="Archit")

# #default argument
# def greet(name="Guest"):
#     print("Hello", name)
# greet("Archit")
# greet()

# #Variable-Length Arguments
# def total(*numbers):
#     return sum(numbers)
# print(total(1, 2, 3))
# print(total(4, 5, 6, 7))


# def form(name,age ):
    # name = input("enter your name : ")
    # age = int(input("enter you age : "))
#     print("name : ",name)
#     print("Age : ",age)

# form(input("Enter your name : "),int(input("enter you age : ")))   

# def form(name , age):

#     print("name : ",name)
#     print("Age : ",age)

# form(name="archit",age=22) 

# def fact(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return num*fact(num-1)   
# print(f"factorial : ",fact(int(input("enter the number : "))))

#write a program to creat a fn which adds min 2 numbers max 5 numbers 
def fsun(*num):
    if 2 <= len(num) <= 5 :
        return sum(num)
    else:
        return "-1"    

print(fsun(1,2))


#write a program to find the sum of individual digits 
# def isum(num):
#     s=0
#     num = str(num)  
#     for digit in num:
#         s += int(digit)
#     return s
 
# print(isum(123))
