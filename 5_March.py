#question-1
# *
#  *
#   *
# for i in range(1,4):
#       for j in range(1,i):
#             print(" ",end="")
#       for k in range(0,1):
#             print("*",end="")
#       print()
#Approach-2
#--------------------------------------------------------------------------------------------------------
#-question-2
# ***
# ***
# ***
# for i in range(1,4):
#       for j in range(1,4):
#             print("*",end="")
#       print()
#----------------------------------------------------------------------------------------------------
#question-3
# ****
# ****
# ****
# for i in range(1,4):
#       for j in range(1,5):
#             print("*",end="")
#       print()

#-------question-4

# enter no. of rows:4
# enter no. of columns:4
####
####
####
####

# row=int(input("enter no. of rows:"))
# column=int(input("enter no. of columns:"))
# for i in range(1,row+1):
#       for j in range(1,column+1):
#             print("#",end="")
#       print()
# IN A MATRIX:left to right diagonal is primary diagonal(here i==j means i and j ki value equal hoti h) and the right to left diagonal is secondary diagonal

#question-5
# *  
#  * 
#   *
# for i in range(1,4):
#       for j in range(1,4):
#             if(i==j):
#                   print("*",end="")
#             else:
#                   print(" ",end="")
#       print()

#question-6
#   *
#  *
# *
# for i in range(1,4):
#       for j in range(3,i,-1):
#             print(" ",end="")
#       for k in range(0,1):
#             print("*",end="")
#       print()


#question-7
# #++
# *#+
# **#

# print # if i==j( PRIMARY DIAGONAL)
# print  * if i > j(UPPER TRIANGLE)
# print + if j > i(LOWER TRIANGLE)

# for i in range(1,4):
#       for j in range(1,4):
#             if(i==j):
#                   print("#",end="")
#             elif(i>j):
#                   print("*",end="")
#             else:
#                   print("+",end="")
#       print()



#question-8
# enter no. of rows4
# enter no. of col4
#    *
#   *
#  *
# *
# print * at the secondary diagonal of a matrix means at right to left diagonal

# row=int(input("enter no. of rows:"))
# col=int(input("enter no. of col:"))
# for i in range(1,row+1):
#       for j in range(1,col+1):
#             if i+j==row+1:
#                   print("*",end="")
#             else:
#                   print(" ",end="")
#       print()



#question-9
# enter no. of rows:3
# enter no. of col:3
# **#
# *#@
# #@@
# print # if i+j==rows+1(SECONDARY DIAGONAL)
# print  * if i+j<rows+1(UPPER TRIANGLE)
# print @  if i+j > rows+1(LOWER TRIANGLE)

# row=int(input("enter no. of rows:"))
# col=int(input("enter no. of col:"))
# for i in range(1,row+1):
#       for j in range(1,col+1):
#             if i+j==row+1:
#                   print("#",end="")
#             elif i+j<row+1:
#                   print("*",end="")
#             else:
#                   print("@",end="")
#       print()


#question-10 
# * $
#  $
# $ @
# row=int(input("enter no. of rows:"))
# col=int(input("enter no. of col:"))
# for i in range(1,row+1):
#       for j in range(1,col+1):
#             if(i+j==row+1):
#                   print("$",end="")
#             elif(i==1 and j==1):
#                   print("*",end="")
#             elif(i==row and j==col):
#                   print("@",end="")
#             else:
#                   print(" ",end="")
#       print()



#question-11
# * $
#  $
# $ *
# row=int(input("enter no. of rows:"))
# col=int(input("enter no. of col:"))
# for i in range(1,row+1):
#       for j in range(1,col+1):
#             if(i+j==row+1):
#                   print("$",end="")
#             elif(i==1 and j==1 or i==row and j==col ):
#                   print("*",end="")
#             else:
#                   print(" ",end="")
#       print()