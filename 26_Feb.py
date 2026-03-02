# Type_Casting

# used for changing the value or datatype of the value
# Syntax--> var_name =Data_type(value)
# complex data type doe not change into other datatype execpt two
# string
# boolean
# single value varaible does not type cast into tuple, list, set, dict
# Boolean datatype convert into two factors
# False === 0
# True === 1
# List cannot be type casted into any single variable datatype except boolean and all mutli value datatype with exception of dict()
# for list to convert into dict()vthese condition must be followed:
# all the values of list must be Multi value datatype
# length of the values must be 2
# for dict typecasting to convert in to other multi value datatype :
# for simple datatype(var_name) only gives key not the values the output show only key of the dict not thwe values
# values() method -->for only values write datatype(var_name.values()) for seeing the values
# items() method --> for both key and values syntax ***datatypes(var_name.items())** for seeing the values and key
# tp = (12,34,[45,56,78])

# int and float
b =5.0

# print(int(b))
# print(complex(b))
# print(bool(b))
# print(str(b))
 
 # complex datatype
c = 5+2j
# print(str(c))
# print(bool(c))
# print((c))

# boolean
d =False
# print(d)
# print(int(d))
# print(float(d))
# print(complex(d))
# print(str(d))


#String datatype
s = 'archit'
sa = 'a'
# print(bool(s))
# print(bool(sa))
# print(list(s))
# print(list(sa))
# print(tuple(s))
# print(tuple(sa))
# print(set(s))
# print(set(sa))
# string type cast
z = '123'
# print(int(z))
# print(float(z))
# print(complex(z))
# print(bool(z))
# print(list(z))
# print(tuple(z))
# print(set(z))

y= '123.34'
# print(float(y))
# print(complex(y))
# print(bool(y))
# print(list(y))
# print(tuple(y))
# print(set(y))

u = '2+4j'
# print(bool(u))
# print(list(u))
# print(tuple(u))
# print(set(u))
# List type casting
li = [1,2,'hi',2,3,3,4]
# print(bool(li))
# print(list(li))
# print(tuple(li))
# print(set(li))

# l2 = ['hi', [2,23],'to',['hi','hello']]
# print(dict(l2))
# print(bool(l2))
# print(list(l2))
# print(tuple(l2))

# l3 =['hi','lo','pp']
# print(dict(l3))
# print(bool(l3))
# print(list(l3))
# print(tuple(l3))
# print(set(l3))
# tuples typecasting
# t1 = ([1,2],(3,4),'hi')
# print(str(t1))
# print(dict(t1))
# print(bool(t1))
# print(list(t1))
# print(tuple(t1))
# print(set(t1))

# set typecasting
# s1 = {1,2,3,(4,5),2}
# s2 ={'hi','lo','pp'}
# print(str(s1))
# print(dict(s2))
# print(bool(s1))
# print(list(s1))
# print(tuple(s1))

# dictory typecasting
# d1 = { 1:45, 'name':'archit'}
# d2 = { 'list': [1,2],1:2}
# print(d2)
# print(str(d1))
# print(bool(d1))
# print(list(d1))
# print(tuple(d1))
# print(set(d1))

# # for values of the dict in typecasting 
# print(list(d1.values()))
# print(tuple(d1.values()))
# print(set(d1.values()))
# # for both values and key of the dict 
# print(list(d1.items()))
# print(tuple(d1.items()))
# print(set(d1.items()))
# m =1,2,2
# # b = float(m)
# c = str(m)
# d = tuple(m)
# e = set(m)
# ss= str([22,23])
# Copy_opreation

# used for copying the data collection
# mainly used in list because all the opreation can be performed
# in string we cannot choose beacuse it is immutable and act as all char as string or eparate
# in tuple we caanot choose because it is immutable
# n set we caanot choose because it does not accept duplicate ad its unorder
# copy are of three type :
# general

# Syntax --> new_var = old_var
# when change the new_var the old_var doesnot get affected
# it copy the content of varaible Space
# it take the varaible reference
# Both variables point to same memory.
# Nested changes affect original for multi value datatype.
# shallow copy

# Syntax --> new_var = source_var.copy()
# it copy the content of value space
# Inner objects are shared it affect the original.
# Nested changes affect original.
# deep copy

# Syntax --> import copy
# new_var =copy.deepcopy(source_var)
# Completely new copy created.
# Fully independent memory.
# general copy
# g1 = [10,20,30]
# l = [10,20,30,[2,3,4]]
# l3 = [1,2,3,[4,5,[6,7,8]]]
# g =g1
# g[2] = 200
# print(g1)

# shallow copy
# s = g1.copy()
# s[2] = 200
# print(s)
# print(g1)

# l2 = l.copy()
# l2[3][2] = 400
# print(l2)
# print(l)

# l5 = l3.copy()
# l5[3][2][1] = 700
# print(l5)
# print(l3)
# deep copy 
# import copy
# d = [1,2,3,43]
# d1 = [1,2,3,[4,5,6]]
# d2 = [1,2,3,[4,5,6,[7,8,9]]]

# dd = copy.deepcopy(d)
# d1d = copy.deepcopy(d1)
# d2d = copy.deepcopy(d2)

# dd[2] = 200
# d1d[3][1] = 400
# d2d[3][3][1] = 400

# print(d)
# print(dd)
# print(d1)
# print(d1d)
# print(d2)
# print(d2d)
# <bound method Kernel.raw_input of <ipykernel.ipkernel.IPythonKernel object at 0x000002032A2B23C0>>
# Operators

# shortcut for operators Alarm Bi:

# Arithmetic
# / + - * // %, **
# Logical
# and, or, not
# Presendence --> not >> and >> or
# Assigment
# !, =, +=, -=, *=, /= //==
# Relational
# <, >, >=, <=, ==, !=
# Membership
# in, not in
# Bitwise
# Identity
# is, is not
# Precedence in single value data : --> bool → int → float → complex

# all the default values are false in the python other than those values are true values of the datatypes

# print(10 and 40)
# print(0.0 and 0)
# print(10 or 40)
# print(0.0 or 2.4)
# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
# print(bool(True))
# print(bool(''))
# print(bool([]))
# print(bool(()))
# print(bool(set()))
# print(bool({}))

# i = 2
# f = 2.0
# c = 3+8j
# b = True
# l = [1,2,3]
# l2 = [7,8,9]
# t = (3,4,5)
# t2 = (7,8,7,6)
# se = {12,23,45}
# se2 ={5,6,7}
# d = { 'a':23 , 'n': 43}
# d2 = { 'pl':234 , 'l': 98}
# st = 'archit'
# st2 = '2adf' 

# assigment
# t+=t2

# # Relational 
# # print(c > 4+9j)
# print(ord('a'))
# print(st < st2)
# print(l2 > l)
# print(l > l2)
# print(t == t2)
# print( t != l2)
# d == d2

# # member
# print(2 not in l2)
# print(3 in t)
# # print(23 in se) beacuse it is unorer
# print(23 in d)
# print('d' in st)

# se == se2
# i is f
# i is not f
# True
#  for converting into binary
# bin(7)
# '0b111'