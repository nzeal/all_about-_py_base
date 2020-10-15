#Advanced python-Object oriented programming
'''
1. objects are methods and attributie that access with the dot method
2. All the data types built into Python are classes.
3. A method is a function within a particular class. As for __init__ method, 
you can define any other method associated to that class. 
'''
'''
Class can instantiate i.e the action of creating different instances
- insttances are objects
- Here are few examples
'''
# Example-0 

class BigCircle: 
    pass

bg = BigCircle()
print(bg)


'''
Encapsulation
'''

# Example-1
class PlayerCharacter:
    # Constructor function
    def __init__(self, name, age):  # self refer to Playercharacter 
        self.name = name
        self. age = age
    
    # Define another method
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Andy',21)
player2 = PlayerCharacter('Michael', 24)

print(player1)
print(player2)
print(player1.name)
print(player1.age)
print(player1.run())

'''
Attributes are the pieces of the date that are dynamics
'''
class PlayerCharacter:
    # class Object attributes (these are dynamics)
    membership = True 
    def __init__(self, name, age):  # self refer to Playercharacter 
        if (PlayerCharacter.membership):
            self.name = name
            self. age = age
    
    # Define another method
    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Andy',21)
player2 = PlayerCharacter('Michael', 24)

print(player1.membership)
print(player1.name)
print(player1.shout())


# General guidelines 

class NameOfClass():
    class_attribute = 'value'
    def __init__(self, param1, param2):
        self.param1 = param1
        self. param2 = param2

    def method(self):
        #code
    
    @classmethod
    def cls_method(cls, param1, param2):
        #code
    
    @staticmethod
    def stc_method(param1, param2):
        #code



'''
Dunder Methods 
'''

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        
    def __str__(self):
        return f'{self.color}'
action_figure = Toy('red', 0)

print(action_figure.__str__())

print(str(action_figure))