# LOOPS
# Loops are used to execute a block of code multiple times.
# Types of loops
# for
# when iteration are given
# initalization is not required
# Syntax -->
# for var in collection:
# statement
# while
# Runs while condition is True.
# Syntax -->
# initialization
# while condition:
# statement block
# # i = 1
# # while i < 20:
# #     print(i)
# #     i+=1


# i = 50
# while i >= 40:
#     print(i)
#     i-=1
# i = 0
# flag = 0
# while flag <= 20:
#     if(i % 2 == 0):
#         print(i)
#         flag += 1
#     i += 1
    


#  reverse string with slicing
# nums = input("Enter the string: ")
# reve = ''
# j = len(nums)-1
# while j >= 0:
#     reve += nums[j]
#     j -= 1
# print(reve)


# table 
n = int(input("Enter the no: "))
i = 1
while i <=10:
    # print(n, 'x', i, '=', n*i)
    print(f"{n} x {i} = {n*i}")
    i+=1


## for loop
# l = [1,2,3,4,5]
# for i in l:
#     print(i,)
print(range(1,10))

# for a in range(1,10,2):
#     print(a, end=' ')

# for i in range(10,0,-1):
#     print(i)


# repalce the space with underscore inside the string
st = input("Enter your text: ")
# st.replace(' ','_')
for i in st:
    if i == ' ':
        print('_', end='')
    else:
        print(i, end='')
range(1, 10)



# Split Function

# Syntax --> Var_name.split(separator, maxsplit)
# l = ['p1.py', 'first.txt','t3.py','tk.txt','tfk.com']
# d = {}

# for i in l:
#     part = i.split('.')
#     print(part)
#     inn = part[0]
#     out = part[1]
    
#     if out not in d:
#         d[out] = []
#     d[out].append(inn)
# print(d)
    
    
    ## second question

# stt1 = 'aaabbaabcc'
# stt2 =''
# i = 0
# while i < len(stt1):
#     char = stt1[i]
#     count = 1
#     while i + count < len(stt1) and stt1[i + count] == char:
#         count += 1
#     stt2 += char + str(count)
#     i += count

# print(stt2)


## third questins
# l = ['aditya', 'archit', 'pradit', 'keshav']
# v =''
# for i in l:
#     for j in i:
#         if j in 'aeiouAEIOU':
#             v+= j
# print(v)
# print(len((v)))


## fourth questions

# l = [(2+3j),12,'Program','Python',False]
# d = {}
# for i in l:
#     if( type(i) == str):
#         # print(i)
#         v = ''
#         for j in i:
#             if j in 'aeiouAEIOU':
#                 v+=j
#         d.update({i:v})
# print(d)



# l = 'prgrom'
# print(isinstance(l,str))