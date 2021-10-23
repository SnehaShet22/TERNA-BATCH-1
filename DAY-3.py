'''
          #  0        1        2 
thisList= ["apple",'cherry','pear']
          #   -3      -2       -1
print(thisList) 

print(thisList[1])
print(thisList[-1])

thisList.append('banana')
thisList.append(['mango','tangerine']) #['apple', 'cherry', 'pear', 'banana', ['mango', 'tangerine']]
thisList.extend(['mango','tangerine'])#['apple', 'cherry', 'pear', 'banana', ['mango', 'tangerine'], 'mango', 'tangerine']
print(thisList)
'''
'''

a = len(thisList)
print(a) 

print(type(thisList))

a = (1,2,3,4,5, 5 , 5 , 5.5 ) 
ab= list(a) 
print(ab) 
'''
          #   0        1        2        3             4                  5          6
thisList= ['apple', 'cherry', 'pear', 'banana', ['mango', 'tangerine'], 'mango', 'tangerine']
'''
print(thisList[:]) #WHOLE LIST 
print(thisList[-1]) #LAST ELEMENT

print(thisList[4]) 


if 'pear' in thisList:
    print("yes 'pear' is in the list" )
else:
    print("not applicable")  
'''
'''
thisList[3] = ' pomogranate '   # REPLACING ELEMENT / UPDATING ELEMENT 
print(thisList)

thisList[2:5 ] = ["Strawberry", "Orange", 'Papaya'] 
print(thisList)                                                       #['apple', 'cherry', 'Strawberry', 'Orange', 'Papaya', 'mango', 'tangerine']

thisList[1:2]= ["grapes", ' mango']   #OTHER ELEMENTS SHIFTED TO RIGHT ['apple', 'grapes', ' mango', 'Strawberry', 'Orange', 'Papaya', 'mango', 'tangerine']
print(thisList)  
                                                                        #  0          1         2 
thisList.insert(2 , 'watermelon' )  #ONLY INSERTING                     ['apple', 'grapes', 'watermelon', ' mango', 'Strawberry', 'Orange', 'Papaya', 'mango', 'tangerine']
print(thisList)  


T = ( "KIWI" , " ORANGE")
thisList.extend(T)
print(thisList)    
'''
'''

thisList=['apple', 'grapes', 'watermelon', ' mango', 'Strawberry', 'Orange', 'Papaya', 'mango', 'tangerine', 'KIWI', ' ORANGE']
thisList.pop(-2)  #thisList.pop(9) 

print(thisList)   #['apple', 'grapes', 'watermelon', ' mango', 'Strawberry', 'Orange', 'Papaya', 'mango', 'tangerine', ' ORANGE']
thisList.pop()    #NO INDEX SO DEFAULT VALUE IS -1  WILL REMOVE LAST ELEMENT 
print(thisList)

del thisList[6]     #['apple', 'grapes', 'watermelon', ' mango', 'Strawberry', 'Orange', 'mango', 'tangerine']
print(thisList)  

#del thisList  #delete whole list 
#print(thisList)

#thisList.clear()
#print(thisList)       #[]   returns empty list 

print(len(thisList))  # 8 

l = ["hii"]*4 
print(l)           #['hii', 'hii', 'hii', 'hii']   

           # 0          1       2        3             4                   5        6
thisList= ['apple', 'cherry', 'pear', 'banana', ['mango', 'tangerine'], 'mango', 'tangerine'] 

print(thisList[4][1])\


i = [    [  [ [  ["i","have","the"]  , ['knowledge','of','programming']  ]   ]   ]    ]

print (i [0][0][0][0][1]   )  #have 

print(i[0][0][0][1][0])    #knowledge 


i  = [  
      [  [ [  ["i","have","the"]  , ['knowledge','of','programming']  ]   ]   ]    # 0
      
      ]

i =     [ 
     [ [  ["i","have","the"]  , ['knowledge','of','programming']  ]                # 0 
       ]

i=  [
     [  ["i","have","the"]  , ['knowledge','of','programming']                     # 0 
      ]

i= [
      ["i","have","the"]  , ['knowledge','of','programming']                       # 0    # 1 
]

i =  ["i","have","the"]              #['knowledge','of','programming']             # 1     #0

i = "have"  #'knowledge'  


s =  ['apple', 'cherry', 'pear', 'banana'] 

for i in range(0 , len(s)):
    print (s[i] )   


i = 0 
while i < len(s): 
    print(s[i]) 
    i += 1 

[ print(i)  for i in s]  # list comprehention 

for i in s :
    print (i )
'''

s =  ['apple', 'cherry', 'pear', 'banana'] 

newlist = [ x for x in s if x != 'apple']
'''
for x in s :
    if x != 'apple':
        newlist.append(x) 
'''
print(newlist)  


s= [1,5,8,6,8,5,78]
print(max(s))     #78

print ( min(s))    #1

print( s.count(8))   # 2 

print ( s.index(6))   #3

y=s.copy() 
print(y)  

y.sort()

print(y) 

y.reverse()
print(y) 

'''
#EXERCISE  

my_list = [100,200,300,400,500,600,700,[100,5,6,5,4,['a','b','c']]] 

print(my_list[7][5][1])  

# 0   1   2   3   4  5    6             7
[100,200,300,400,500,600,700,[100,5,6,5,4,['a','b','c']]]    #7 
# 0  1 2 3 4       5
[100,5,6,5,4,['a','b','c']]                                  #5 
# 0   1    2
['a','b','c']                                                #1


print(my_list[-1][-1][1])  

nes= [[['hello','welcome',33]],[[222,333,444]]]  #ACCESS WELCOME 

#welcome 
                        # 0 
i=  [       [['hello','welcome',33]],[[222,333,444]]      ]    #0

#                    0                    1
i= [      ['hello','welcome',33]],[[222,333,444] ]             #0
#   0        1      2
['hello','welcome',33]                                         #1

#333
                        # 0              # 1                   #0
i=  [       [['hello','welcome',33]],[[222,333,444]]      ]    #1

#                    0                    1
i= [         [[222,333,444]   ]                                #0
#   0        1      2

# 0   1   2   
[222,333,444]                                                  #1              


 [[['hello','welcome',33]],[[222,333,444]]    #0

 [['hello','welcome',33]],[[222,333,444]]     #1

 [[222,333,444]]                              #0 

 [222,333,444]                                #1 

''' 