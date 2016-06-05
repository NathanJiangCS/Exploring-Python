#This is more of a programming term than a python specific topic

'''
A programming language is said to have a first class function if it treats
functions as an entity which supports all the operations generally available to other
entities. These operations typically include being passed as an argument, returned
from a function, and assigned to a variable.

A higher order function is a function that either accepts other functions as an
argument or returns a function as a result
'''

def square(x):
    return x*x

#We can set our variable f equal to the function
#We do not need () or any arguments because that means we are calling the function and
#that is not what we wanted to do.
f = square
print f #gives us <function square at 0x101178950>
#This is what it means to be a first class function as we now can treat f as a function

print f(5) #returns 25

#We can also pass functions as arguments
#An example of this is the map function that takes a function and an array as the argumetns
#and then returns a new array of the values of the original array put through the function.
#This is a self-made map function to see the functionality

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5]) #We are passing in the square function above
                                      #as an argument


#We can also return functions as the result of other functions
def logger(msg):

    def log_message():
        print('log:' msg)

    return log_message
#We are returning the function log_message 
log_hi = logger('Hi') #This returns log_message but it remembers our initial msg that was given
print log_hi #This prints our function log_message, not the log result
log_hi() #This actually gives us 'log: Hi'
