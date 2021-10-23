#TUPLE 
'''
#tuple is always in round brackets () 
             #  0        1         2        3
thisTuple = ("apple", 'banana', 'mango', 'apple') 
print(thisTuple)              #('apple', 'banana', 'mango','apple)
print(type(thisTuple))        #<class 'tuple'> 

print(len(thisTuple))    #4


# CREATE TUPLE WITH ONLY 1 ELEMENT 
#TO CREATE A TUPLE WITH ONLY ONE ITEM , YOU HAVE TO ADD COMMA AFTER THE ITEM , OTHERWISE PYTHON WILL NOT RECOGNIZE IT AS TUPLE
this_Tuple = ("apple") 
print(type(this_Tuple))  # <class 'str'> 

this_Tuple = ("apple",) 
print(type(this_Tuple))  #<class 'tuple'> 

#TUPLE CAN HAVE DIFFERENT DATA TYPES 
thisTuple = ("apple", 'banana', 'mango', 'apple') 
tup = (1,2,3,5.5,6.0 ,3, True,False, 'FYGFYT')
 

#TYPE CASTING 
A= [100,200,300,400,500,600,700,[100,5,6,5,4,['a','b','c']]] 

thisTuple = tuple(A)

print(thisTuple)       #(100, 200, 300, 400, 500, 600, 700, [100, 5, 6, 5, 4, ['a', 'b', 'c']])
print(type(thisTuple)) # <class 'tuple'>   



             #  0        1         2        3
thisTuple = ("apple", 'banana', 'mango', 'apple')  
print(thisTuple[3])     #apple 

print(thisTuple[-2])    #mango   


   # 0   1    2    3    4    5    6                  7 
s=(100, 200, 300, 400, 500, 600, 700, [100, 5, 6, 5, 4, ['a', 'b', 'c']])  

print(s[3:7])  # (400, 500, 600, 700)

# the search index will start at 3 (included) and end at 7 (excluded)(only print till 6)  

print(s[:])   # prints whole tuple 
s.count(100)  #1  

#REVERSE METHOD
print(s[::-1])  #([100, 5, 6, 5, 4, ['a', 'b', 'c']], 700, 600, 500, 400, 300, 200, 100) 

#[::-1]           [START  :  LENGTH (SEQUENCE ): COUNT ]      COUNT=1 BY DEFAULT 
# ABOVE COUNT IS -1 


if 200 in s :
    print("its present")
else:
    print("not present") 

if 200 not in s :
    print("its not present")
else:
    print(" present")   


thisTuple = ("apple", 'banana', 'mango', 'apple') 
#thisTuple[3]= 'kiwi'    #'tuple' object does not support item assignment
print(thisTuple)         

#WORKAROUND TO UPDATE TUPLE

a= list(thisTuple)  #COVERT TUPLE TO LIST
a[3]= 'kiwi'        # UPDATE LIST 
thisTuple= tuple(a) # COVERT LIST BACK TO TUPLE
print(thisTuple)    #('apple', 'banana', 'mango', 'kiwi') 




thisTuple = ("apple", 'banana', 'kiwi') 
#UNPACKING 

(red , yellow , green ) = thisTuple

print(red)     #apple
print(yellow)  #banana
print(green)   #kiwi 


thisTuple = ("apple", 'banana', 'kiwi') 
#UNPACKING 

(red , yellow , green ) = thisTuple

print(red)     #apple
print(yellow)  #banana
print(green)   #kiwi 


s =('apple', 'grapes', 'watermelon', ' mango', 'Strawberry', 'Orange', 'mango', 'tangerine')
(red , yellow , green ) = s 
#ValueError: too many values to unpack (expected 3)
print(red)     
print(yellow)  
print(green)


#USE ASTREIK IF YOU WANT TO PRINT ALL ELEMENTS 
s =('apple', 'grapes', 'watermelon', ' mango', 'Strawberry', 'Orange', 'mango', 'tangerine')
(red , yellow , *green ) = s 

print(red)     #apple
print(yellow)  #grapes
print(green)   #['watermelon', ' mango', 'Strawberry', 'Orange', 'mango', 'tangerine']   

#USE ASTREIK IF YOU WANT TO PRINT ALL ELEMENTS 
s =('apple', 'grapes', 'watermelon', ' mango', 'Strawberry', 'Orange', 'mango', 'tangerine')
(red , *yellow , green ) = s 

print(red)     #apple
print(yellow)  #['grapes', 'watermelon', ' mango', 'Strawberry', 'Orange', 'mango']
print(green)   #tangerine

#IF THE * IS ADDED TO ANOTHER VARIABLE NAME THAN THE LAST , PYTHON WILL ASSIGN VALUES TO THE VARIABLE UNTIL
#THE NUMBER OF VALUES LEFT MATCHES THE NUMBER OF VARIABLES LEFT
'''
#ITERATING THROUGH FOR LOOP
thisTuple = ("apple", 'banana', 'kiwi') 
for x in thisTuple:
    print(x) 

for i in range(0,len(thisTuple)):
    print(thisTuple[i])  


#ITERATING THROUGH WHILE LOOP 
thisTuple = ("apple", 'banana', 'kiwi')  
i= 0 
while i < len(thisTuple):
    print(thisTuple[i])
    i +=1 


#tuple CONCATENATION 
tup= ('a','b','c')
tup1 = (1,2,3)
tuple1 = tup + tup1 
print(tuple1)     #('a', 'b', 'c', 1, 2, 3)  

#TUPLE MULTIPLICATION 
thisTuple = ("apple", 'banana', 'kiwi')  
T= thisTuple*2 
print(T)      #('apple', 'banana', 'kiwi', 'apple', 'banana', 'kiwi')  


thisTuple = ("apple", 'banana', 'kiwi','APPLE','apple')  

print(thisTuple.count("apple"))   # 2 

print(thisTuple.index("apple"))   #0  


