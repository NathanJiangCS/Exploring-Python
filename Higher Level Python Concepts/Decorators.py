#Decorators are functions that take another function as an argument, add some
#type of functionality, and then returns another function. All this without
#changing the source code of the function that is passed in

######################################
#Basic example.
#Decorator functions allow us to add functionality to functions easily.
#We simply add code to the wrapper function which adds more functionality to
#a desired function.
def decorator_function(original_function):
    def wrapper_function():
        print 'This executes before {}'.format(original_function.__name__)
        return original_function()
    return wrapper_function


def display():
    print 'display function ran'

#Pass in display function to decorator function which returns the wrapper function
#that, when called, carries out the original function (display).
decorated_display = decorator_function(display)
decorated_display() 

#We can add @decorator_function (the decorator function we want) before the declaration
#of the original function so that whenever the original function is called, it actually
#executes the decorated version of the original function
#An example included below

@decorator_function
def hello_world():
    print 'hello world!'
#This function declaration is essentially the same as hello_world = decorator_function(hello_world)


hello_world()
#This prints out:
#This executes before hello_world
#hello world!
#Because the hello world function is refered to the decorator function which adds the first line

######################################
#More advanced example
#In the example above, it wouldnt work if the original function took in any arguments
#Therefore, we add * and ** as arguments to our wrapper function

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs): #By adding these, it allows it to accept any arbitrary number of
                                           #arguments for the function
        print 'This executes before {}'.format(original_function.__name__)
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print 'display function ran'
    
@decorator_function
def display_info(name, age):
    print 'display_info ran with arguments ({}, {})'.format(name,age)

display_info('Nathan', 100) 

######################################
#Using classes as decorators instead of functions

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function #Ties the original function with the instance of this class

    def __call__(self, *args, **kwargs):
        print 'This executes before {}'.format(original_function.__name__)
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print 'display function ran'
    
@decorator_class
def display_info(name, age):
    print 'display_info ran with arguments ({}, {})'.format(name,age)
