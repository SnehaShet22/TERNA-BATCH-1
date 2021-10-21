#GLOBAL VARIABLE

'''
x ='awesome'

def myfunction():
    print(x) 

myfunction()  




def myfunction():
    global x
    x ='awesome'
    print(x) 


myfunction()  
print(x)  


'''  
#STRING 
'''

a = "HELLO WORLD"            # 0 1 2 3 4 5 6 7 8 9 10
                             # H E L L O   W O R L D
                             #-11-10-9-8-7-6-5-4-3-2-1            

print(a[1])    a[8]  a[4]
print(len(a))


print(a[10])
print(a[-1])

for i in a:
    print(i) 
                                # a[:]

if 'O' not in a :
    print("o is present in a")

else:
    pass 
'''
'''
#SLICING 

a = "HELLO WORLD" 

print(a[2:5])         # (start : end+1) 

b = a[:]              # [  start  :  len(string )]   (start : len(string): count=1 )

print(b)

c= a[:4]
print(c) 

d= a[6 : ]
print(d)  

# NEGATIVE INDEXING 

print ( a[-5:-2])


'''

'''
a = "Hello  World" 

b=a.upper()

b=a.lower()

c = a.strip()


print(a.strip()) 
print(a.replace(" ",""))


# replace method 
print(a.replace("l","A"))

#SPLIT METHOD 


a = "Hello , World" 

print(a.split(","))

print(a.split("l"))   #['He', '', 'o , Wor', 'd'] 

'''
'''
a= "Hello"
b="world" 
c= a +' '+ b
print(c) 

a= "Hello"
b= '1234.55'  
c= a + b
print(c) 

#format method 

age = input(" tell us your age  :  ")
txt= "MY NAME IS JOHN, AND I AM {}" 
print('\n')
print(txt.format(age))



quantity = 3
item_no = 567
price = 50 

my_order = " I WANT {0} PIECES OF ITEM {1} FOR {2} DOLLARS"

print(my_order.format(quantity,item_no,price))

''' 

'''
txt = 'we are the so-called \'vikings\' from the north.'

a= "helLo worlD"
b=a.center(5)    #helLo worlD
print(b) 
'''
'''

a= "helLo worlD"

b= a.count("l") 
print(b) 

b=a.encode()
print(b)  

b= a.find("l")
print(b)

print(a.swapcase())   #HELlO WORLd




print(10>9)
print(10==9)
print(10<=9) 

'''

a= 200 
b= 33 

if b>a:
    print(b," is greater than ",a)  #  b+"is greater than" +a

else:
    print(b," is less than ",a) 


print(bool(""))
print(bool(0)) 
print(bool([]))  
print(bool(())) 
print(bool({}))  

def fun ():
    return True 

print(fun())



a = "HELLO WORLD" 
print(a[::2])       #H L O W R D