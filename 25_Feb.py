# DIR
## give the all the function in the current file
# print(dir())
# dir(str)

# print(dir(list))

# print(dir(tuple))

# print(dir(set))

# print(dir(dict))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# List

# Ordered Collection
# it can sotre values of the data or data collection
# it is hetrogenous and homogeneous
# it is enclosed btw squared bracket []
# it is mutable data collection type
# Syntax--[ ]
# l = [ 1,2,3,4,'as']
# default value : [ ] empty
# duplicate values
# Mehtod in List
# there are 11 method in list
# Append Syntax-->  var_name.append(value)
# insert Syntax -->   var_name.insert(index, value)
# remove & pop Syntax -->   var_name.pop()   or   pop(index)   var_name.remove(value)
# pop() --> this remove last element & pop(index) --> remove the index element
# remove() --> this remove from checking the value of the list not the index
# clear Syntax--> var_name.clear() clear the list
##List example
# l = ['archit', 706, '25/06', 21]
# print(type(l))
# print(list())
# print(l[1])
# l[1] = 707

# list memory explain
# l2 = [100,200, 'hi', 'hello', False]
# print(id(l2))
# print(id(100))
# print(id('hi'))
# print(id('hello'))
# print(id(l2[3]))
# print(id(l2[3][0]))
# print(id(l2[3][1]))
# print(id(l2[3][2]))
# print(id(l2[3][3]))
# print(id(l2[3][4]))
# print(hex(id(l2[3][0])))
# print(hex(id(l2[3][1])))
# print(hex(id(l2[3][2])))
# print(hex(id(l2[3][3])))
# print(hex(id(l2[3][4])))
# print(id(False))
    
# access value in value 
# print(l2[3][3])

 # method in list
# append and insert
# l.append(40)
# l.insert(2,'lo')
# print(l)
# l.remove('lo')
# l.pop(4)
# ['archit', 706, 'lo', '25/06', 21, 40]
# 40
# lis = ['Python is not easy']
# print(lis[0][14])
# print(lis[0][-4])
# print(lis[0][10])
# print(lis[0][-8])
# print(lis[0].count('o'))
# e
# e
# n
# n
# 2
# Tuples

# Ordered Collection
# collection of homogenous and hetrogenous data types
# it is immutable datatype
# it stored in paranthesis ( )
# Syntax--> var_name = (1,2,3,4 ,.......) or var_name = 1 ,2, ,3 ,4,4
# duplicate value is allowed
# tuple requied mor ethan one value to be sotred or one value you have to pass a comma
# default value of tuples() is ( )
# it have two method:
# count
# index
# lt = [1]
# pl = (2,)
# var = ('archit', 706, 21, 'jecrc')
# tup = 1 , 2, 3, 4
# print(type(var))
# print(type(tup))
# print(tuple())
# print(type(lt))
# print(type(pl))
# print(var[0])
# print(var[0].count('a'))
# archit
# 2

# SET
# unordered Collection means there is no indexing
# collection of homogeneous and hetrogeneous
# mutable datatypes
# set stored immutable types of values like string, single values, tuples
# it does not allow duplicates
# Syntax --> var = { 1,2,3, 4}
# default values of(set()) set{} is set()
# method of set
# add Syntax--> var_name.add(value) --> add the values in the set at random position
# pop and remove:-->
# pop --> Syntax --> var_name.pop() pop the values from th set htat are shown at the fornt or 0 index
# remove --> Syntax --> var_name.remove(value) --> remove the element from the set that values is given
# update Syntax --> var_name.update([value]) --> add multpile vlaues in the set
# st = {1 ,2,3,4,5,6,17,8,15,0}
# s = {10, 2.5,(3+2j), 'hi'}
# print((st))
# print(s)
# s.add(20)
# print(s)
# s.pop()
# print(s)
# s.remove('hi')
# print(s)
# {0, 1, 2, 3, 4, 5, 6, 8, 15, 17}
# {(3+2j), 10, 2.5, 'hi'}
# {2.5, 'hi', (3+2j), 10, 20}
# {'hi', (3+2j), 10, 20}
# {(3+2j), 10, 20}
# s = {1, 2, 3}
# s.update([4, 5])
# print(s)
# {1, 2, 3, 4, 5}



# Dictionary
# A dictionary stores data in key : value pairs.
# Keys must be unique
# Keys must be immutable (string, number, tuple)
# Values can be anything
# Syntax --> var = { key : value, key1 : value1, .........}
# default values of the dictionary dicr() --> { }
# it method :
# clear → Removes all key-value pairs.
# copy → Creates shallow copy dictionary.
# fromkeys → Creates dictionary with default values.
# get → Returns value safely without error.
# items → Returns all key-value pairs.
# keys → Returns all dictionary keys.
# values → Returns all dictionary values.
# pop → Removes key and returns value.
# popitem → Removes last inserted key-value pair.
# setdefault → Inserts key if missing.
# update → Adds or updates key-values.
# d ={ 'name' : 'Archit', 'age' : 22 }
# print(d)
# print(type(d))
# print(d['name'][2])
# print(d.get('place'))
# print(d.get('name'))
# d['age'] = 23
# print(d.items())
# d['place'] = 'jaipiur'
# print(d.items())
# d
# {'name': 'archit', 'age': 21}
# <class 'dict'>
# i
# None
# archit
# dict_items([('name', 'archit'), ('age', 23)])
# dict_items([('name', 'archit'), ('age', 23), ('place', 'jaipiur')])
# {'name': 'archit', 'age': 23, 'place': 'jaipiur'}
# Practise
# practice questionds
# a=[10,2j,'python',[2+5j,11,22.22]]
# print(a[2])
# print(a[-2])
# print()
# b="Python is hard as well as easy"
# b.index('w')
# i = len(b)-b.index('w')
# print(i)
# print(b[18])
# print(b[-12])
# l =['python','Is','Not','Easy']
# print(l[2][0])
# print(l[-2][-3])
# python
# python

# 12
# w
# w
# N
# N
# Slicing

# it is used to extract a part of the collection
# Syntax --> var_name[start:end:step]
# s = 'python'
# print(s[0:9:1])
# print(s[0::1])
# print(s[::1])
# print(s[:])
# print(s[::-1])
# print(s[::-2])
# print(s[:-1])
# c = 'archit Paliwal hello'
# c[::2]
# c[5::-1]
# c[13:6:-1]
# c[7:-6]