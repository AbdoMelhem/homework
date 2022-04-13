#This is a test to show how to commit and push

#Task 01:
'''
def longer_string(n,m):
    #print(n)
    #print(m)
    if len(n)>len(m):
        return (n)
    elif len(n)==len(m):
        return (n)
    else :
        return (m)
  
x=input('First string: ')
y=input('Second string: ')
print('the return result: ',longer_string(x,y))
'''
#--------------------------------------------------------------------------------
#Task 02:
'''
def is_odd(a):
    if a%2!=0:
        print('True, the number that you enterd is odd')
    else:
        print('False, the number that you enterd is even')
    return

a=input('Please enter a number: \n')
a=int(a)

is_odd(a)
'''
#----------------------------------------------------------------------------
#Task 03:
'''
#03.1: For loop
def hello_world_n(n):
    for i in range(n):
        print('Hello World!\n')
    return


#03.2: While loop
def hello_world_n(n):
    i=0
    while i<n:
        print('Hello World!\n')
        i+=1

n=input('\n Enter the number of reapition: \n')
n=int(n)

hello_world_n(n)
'''
#------------------------------------------------------------------------------
#Task 04:
'''
def sum_list(myList,n): #This function is to calculate the sum of items in a list
    sum_fun= 0
    for i in range(n):
        sum_fun = sum_fun + myList[i]
    print('sum_fun= ',sum_fun) 
    return(sum_fun)
'''

'''
# First methode to fill a list:
n=int(input('\nEnter the size of list:\n')) # First -> the size of the list
myList=[] # Second -> Defining the list
for i in range(0,n): # Third -> Filling the list or more accurate -> Adding items to the list
    print('Enter the list item with the index ',i)
    num=int(input())
    myList.append(num)
'''
'''
# Second methode to fill a list:
myList=input('Enter the list items\n').split() # Defining and filling a list. Note the input will be as strings
print('myList= ',myList) 
n= len(myList) # Extracting the number of items in a list
print('num_of_items= ',n)
for i in range(n): # Changing the type of the items in the list to number (integer)
    myList[i]=int(myList[i])
print('myList_as_numbers',myList)
'''
'''
print('sum_main=',sum(myList))

assert sum(myList)==sum_list(myList,n)
'''
#------------------------------------------------------------------------------
#Task 05:
'''
def comparison_fun(randomList,n,m): # This function is to compare items in a list with certin number
    for i in range(n):
        if randomList[i]>m:
            print('The List item > the number you entered is: ',randomList[i])
        


randomList= input('Enter the list items: ').split() # Defining and filling a list. Note the input will be as strings
n=len(randomList) # Extracting the number of items in a list
print('randomList',randomList)
n= len(randomList)
print('num_of_items= ',n)
for i in range(n): # Changing the type of the items in the list to number (integer)
    randomList[i]=int(randomList[i])

print('randomList_as_numbers= ',randomList)
m=int(input('\nEnter the number you want to compare with:\n'))
comparison_fun(randomList,n,m)
'''
#-----------------------------------------------------------------------------
#Task 06:
# 6.01:
'''
def max_fun(maxList,n): # This function is to find max value in maxList
    max=maxList[0]
    for i in range(n):
        if maxList[i]>max:
            max=maxList[i]
    return(max)

maxList=input('Enter the list items: ').split() # Defining and filling a list. Note the input will be as strings
n=len(maxList) # Extracting the number of items in a list
for i in range(n): # CHanging the type of the items in the list to number (integer)
    maxList[i]=int(maxList[i])
print('maxList= ',maxList)
max_value= max_fun(maxList,n)
print('The max value of the List is: ',max_value)
'''

# 6.02:
'''
def long_str(str_List,n): # This function finds the longest String in a list
    longest_str=str_List[0]
    for i in range(n):
        if len(str_List[i])>len(longest_str):
            longest_str=str_List[i]
    return(longest_str)


str_List=input('Enter the list items: ').split() # Defining and filling a list. Notice the input will be as strings
print('str_List= ',str_List)
n=len(str_List) # Extracting the number of items in a list
longest_string=long_str(str_List,n)
print('The longest string in the list is: ', longest_string)
'''
#--------------------------------------------------------------------------------------------
#Task 07:
'''
def division_function(n,k):
    m=0
    for i in range(1,n+1):
        if i%k==0:
            print('The number is: ', i)
            m=m+1
        
    return(m)


n=int(input('Enter the number you want to divide: ')) # Caution: the number should be positive. Q: How to include negative number too?
k=int(input('Enter the number you want to divided by: '))
m=division_function(n,k)
print('the number of division times is: ',m)
'''