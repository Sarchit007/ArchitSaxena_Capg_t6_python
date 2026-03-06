# In Python, variables can be global or local depending on where they are defined.


'''
s1. Global Variable:-
->Declared outside any function.
->Can be used anywhere in the program.

2. Local Variable:
->Declared inside a function.
->Can be used only inside that function.

global Keyword:
->Used to access or modify a global variable inside a function.
->The variable must be declared outside the function.

nonlocal Keyword:
->Used to modify a variable in the nearest outer (enclosing) function.
->Works only with nested functions.
'''

# a = 500  # global variable

# def fname():
#     # global a  // global kw can be used to change the global scope 
#     b = 50
#     a = 50 # assigned new value to a
#     print(b)
#     print(a+b)
#     def fname2():
#         # nonlocal b 
#         b=300
#         print(b)
#     fname2()
# fname()
# print(a)


#create a fn take input as list and find out the product of the element :
# def pro():
#     a = input("enter the element for the list").split()
#     p = 1
#     for i in a
#         p*=int(i)
#     print(p)    


# pro()


#write a program to print the index value of the char present in the given string 
# def prt():
#     st = input("enter the string: ")
#     ch = input("enter the character you want to find in the string :")
#     res = -1
#     for i in range(len(st)):
#         if st[i]==ch:
#             res = i
#             print(i)
    
# prt()



'''
Packing and Unpacking 

'''
# single(tuple)packing example:
def prt(v,*t):
    res = -1
    for i in range(len(t)):
        if st[i]==v:
            res = i
            print(t)
            print(i)
    
prt(100,20,60,80,100,120)


# def in_index(v,*t):
#     print(v)
#     return t
# print(in_index(100,20,60,80,100,120))

# dict packing example 
# def in_index(**d):
#     return d
# print(in_index(a=10,b=20,c=30,d=40))    


def in_index(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
    
in_index(*[5,6,4,8])    
