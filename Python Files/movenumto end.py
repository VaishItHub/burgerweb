
# list=[10,20,3,0,3,0,4,5]
# for i in list:
#     if i==0:
#         list.remove(i)
#         list.append(i)
# print(list)
# ---------------------------
# i=1
# while True:
#     if i%3==0:
#         break
#     print(i)
#     i+=1
# output=
# 1
# 2

# findout common letter between two string
# s1="vaishnavi"
# s2="vaishali"
# print(set(s1))
# print(set(s2))
# -------------------------------------------
# python code for count frequency of the words
# s1="Today at 9:30 pm"
# num = ''.join(filter(lambda x: x.isdigit(),s1))
# print(num)
# -----------------------------------------------
# create dictionary
# Name="Vaishnavi","Shamal","Radha","Mira"
# Marks=90,89,95,90
# dict={Name[i]:Marks[i] for i in range (len(Name))}
# print(dict)

# Fruites="Apple","Banana","Orange","Kevi","Papaya"
# Item=1,2,3,4,5
# dict={Fruites[i]:Item[i] for i in range (len(Fruites))}
# print(dict)
# -----------------------------------------------------------
# findout only digits from the string
# strings="My Bhirth Date is 04/08/2002"
# digit=[str for str in strings if str.isdigit() ]
# print(digit)
# ---------------------------------------------------------------
# Fruites="Apple","Banana","Orange","Peru","Papaya"
# Item=1,2,3,4,5
# dict={Fruites[i]:Item[i] for i in range (len(Fruites))}
# print(dict)
# Fru="Apple Banana Orange Peru Papaya"
# sta=Fru.startswith("Peru")
# print(sta)

# pattern

# for i in range(5):
#      for j in range(0,i):
#          print(("*"),end=" ")
#      print(" ")
# output:-
# *      
# * *    
# * * *  
# * * * *

# single for loop
# n=5
# for i in range(n):
#     print((n-i)* " " ,(i*" *"))
# output:-
#       *
#      * *
#     * * *        
#    * * * *  
# n=5
# for i in range(n):
#     print((n-i)* " ", (i*"*"))
#     output:-
#      *
#     **
#    ***
#   ****