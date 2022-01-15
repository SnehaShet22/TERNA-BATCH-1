#PYTHON LOOPS 
# IF - ELSE
# WHILE LOOP 
# FOR LOOP 

a = 33 
b = 200 
if b > a:
    print('b is greater than a') 
else:
    print('a is greater than b')


a = 33 
b = 33 
if b > a:
    print('b is greater than a') 
elif a == b :
    print('a is equal to b')
else:
    print('a is greater than b') 
    

if b > a:print('b is greater than a') 
elif a == b : print('a is equal to b')
else: print('a is greater than b') 


a =30
b = 30 
print(a) if a > b else print('=') if a == b else print(b) 


# AND - true if and only if both condition true
# OR  - false if and only if both condition false
# NOT - for true it will be false and vice versa 

'''
AND *
0  0 = 0
0  1 = 0
1  0 = 0
1  1 = 1

OR +
0  0 = 0
0  1 = 1
1  0 = 1
1  1 = 1

NOT 
0 = true
1 = false

'''
# AND 
a = 200 
b = 33 
c = 100 
if a > b and c>a :
    print ('both conditions are true')
else:
    print ('both conditions are not true') 

# OR
a = 200 
b = 33 
c = 100 
if a > b or c>a :
    print ('both conditions are true')
else:
    print ('both conditions are not true') 

# nested if 

x = 41 
if x > 10 :
    print ('Above 10') #
    if x > 20 :
        print('and also above 20!') 
    else:
        print('but not above 20') 

# pass 
if x is not 41 : 
    pass 

# FUNCTIONS 

def printing ():
    print ('hii everyone') 

printing() 



def addition (a , b) :
    return a+b    # throws answer outside function

c = addition (5 , 6)  # variable c catches that answer

print(c)

def addition (a , b) :
    return a+b    # throws answer outside function

print(addition (5 , 6)) 

'''
def myfunction (fname):
    print ( fname , 'References')

child1 = 'Emily'
child2 = 'Tobias' 
child3 = 'Linus' 

#myfunction(child1 , child2) # myfunction() takes 1 positional argument but 2 were given
myfunction(child2)
myfunction(child3) 
'''
def myfunction (child):
    print ( child, 'References')

child1 = 'Emily'
child2 = 'Tobias' 
child3 = 'Linus' 

myfunction((child2,child1,child3))  #(child2,child1,child3)

def myfunction (child3 , child2 , child1):
    print ( child3, 'References')

myfunction(child1='Emily',child2='Linus', child3='tobias') 

def myfunction (**child):
    print ( child['fname'], 'References')

myfunction(fname = 'Emily' , lname ='referances') #{'fname': 'Emily', 'lname': 'referances'}


def myteacher (name='Sneha Shet'):
    print ("Hii Everyone , I'm",name) 

myteacher('Shreya')
myteacher() 


def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana","cherry"]

my_function(fruits)

'''

write a program to calculate age of person 
your input will be in form of days. 

ex days = 365 , age = 1 
   days = 2920 , age = 8 
'''

def calculate_age (days):
    return days/365 

calculate_age (2920) 

'''
convert minutes to seconds 
take minute as input 


def minutes (minute):
    return minute * 60

print(minutes(60))
c = minutes(60) 
print(c)


def sec(min):
    min = min/60
    print("Your min value is: ", min)
    return int(min)

b = int(input("Enter seconds: "))

print(sec(b))
'''
'''
*
* * 
* * * 
* * * * 

i = rows    1 2 3 4
j = column  1 2 3 4
'''


for i in range(3):
    print('* * * *')
    if i!=2:
         for j in range(2):
             print('*') 

def pattern (n) :
    for i in range (0,n):
        for j in range (0,i+1):
            print('*',end=' ')
        print('\n')

pattern(5)
