#------------------------------------------------------------------------!
#-- Even you want to write anything you need a langaguage                !
#-- Just like when you speak english there is set of rules               !    
#-- You do followed to speak a good english or any other langague        !
#-- Having said that you do need a langauge talk to computer             !
#-- Choose the langauge in which you want to speak                       !
#-- All right ..this is the breif note to start with                     !
#------------------------------------------------------------------------!

#-- Python Essentials 
    # Data types 
    # Slicing 
    # List comprehension
    # Lambda functions
    # Object Oriented Programming

#Data types
'''
1. int
2. float 
3. booleans 
4. str
5. list
6. tuple 
7. set
8. dictionary 

print(type(6))
print(type(2/4))
round(5.1)
print(round(5.1))
print(bin(5))
print(int('0b101', 2))
print("hello")

#---variables--
# For the best practises 
   # start with lower case or underscore 
   # Letters, numbers. underscores 
   # Case sensitive 
   # snake_case
   # Donot overwrite keywrods 
x = 2020
#---augmented assigments operator
x += 2
x -= 2
print(x)

#--String
usr_name='some body'
print(usr_name)

# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

#--type conversion 
print(type(str(100)))
print(type(int(str(100))))
#---Experssions vs statements 
# Expressions is the actions that produces value (iq/100)
# Statements are entire line of code that perform action  
iq = 100 
usr_age = iq/100

#Booleans 
# True or False 
name = 'somebody'
is_cool = True
is_cool = False
print(is_cool)
print(bool(1))

#List: is an ordered sequence of objects that can be of any types
    #- it is the form of list
    #- it is mutable 
    #- [] squre brackets 

li = [1,2,3,4]
li2 = ['a', 'b']
li3 = [1,2,3, 'n', 's', True]

#Data structure
apple_cart = ['iphone', 'macbook', 'watch']
print(apple_cart[0])  # index start fromm 0 in python
print(apple_cart[1])
print(apple_cart[2])

# List slicing
apple_cart.append('Airpod')
apple_cart[0] = 'Nothing'
print(apple_cart)
print(apple_cart[1:3]) 
print(apple_cart.pop(0)) # removes del apple_cart.pop(0) # removes

'''
# Matrix in python 

my_matrix = [
    [1,2,3],
    [4,5,3],
    [2,6,3]
]
# print(my_matrix[2][1])

# -- List unpacking 
a,b,c = [1, 2, 4]  # 1, 2, 4
print(b)
a,b,c, *other = [1, 2, 4, 5, 6, 7, 8]
print(other)

#Dictionary; in other languages are known as associative array or a map
# it can hold any data types
# It stores key (string), value pair objects.
# Dictionary keys need to have a special property 
# a key needs to be immutable 

dictionary = {
    'a' : 1,
    'd' : 2,
    'c' : 3
}

dictionary = {
    'a' : [1, 2 , 3],
    'd' : 'Dog',
    'c' : True
}
print(dictionary.get('a'))

#Tuples are immutable list. you can not modified (sort, append etc)
#you can access it through index
#because they are less felixble than list, they are usually faster
#count, index
my_tuple = (1,2,3,4,5)
my_tuple[1]
print(5 in my_tuple)

user = {
    (1,2) : [1,2,3],
    'greet' : 'hello',
    'age'   : 20
    }

print(user[(1,2)])
print(my_tuple.count(5)) print(my_tuple.index(5))print(len(my_tuple))

#Function #DRY -> do not repeat yourself
def say_hello(name, emoji):
    print(f'Hello {name} {emoji} ')

say_hello('Somebody', ':)')

def add(a,b):
    return a +b
print(add(5,5))

#---Clean code
def is_even(num):
    if num % 2 ==0:
        return True 
    elif num %2 != 0:
        return False

def is_even(num):
    if num % 2 ==0:
        return True 
    else:
        return False

def is_even(num):
    return num % 2 ==0

print(is_even(27)) 

def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10,1,2,3,4,8]))

#Concept of *arg & **kwargs

def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))

#---Clean code
#Classes -> custom types 

#Specialized Data type, we can use from libraries
