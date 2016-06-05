#Closures

'''
Closures are a record storing a function together with an environment: a mapping
associating each free variable of the function with the value or storage location
to which the name was bound when the closure was created. A closure, unlike a plain
function, allows the function to access those captured variables through the closure's
reference to them, even when the function is invoked outside their scope.
'''

#Example 1
def outer_func():
    message = 'Hi'

    def inner_func():
        print message #this message variable is a free variable because
                      #it is not actually defined within the scope of inner_func
                      #but it is still able to be accessed 

    return inner_func() # we are returning the executed inner function

outer_func() #the result is it prints Hi

#Example 2
def outer_func():
    message = 'Hi'

    def inner_func():
        print message 

    return inner_func #This time, we will return inner_func without executing it

my_func = outer_func() #Now, instead of printing hi, we get that the value of
                       #my_func is the inner_func()
my_func() #We can execute the variable as a function and it prints hi
#This is interesting because we are done with the execution of the outer_func but it
#still is able to access the value of what the message is. This is what a closure is

'''
In simple terms, a closure is a function that has access to variables created in the local
scope even after the outer function is finished executing.
'''

#Example 3
#this time, let us give our functions parameters
def outer_func(msg):
    message = msg
    
    def inner_func():
        print message
        
    return inner_func

hi_func = outer_func('Hi') #This time, the hi and hello func are equal to inner_func
                           #which is ready to print the message
hello_func = outer_func('Hello')

hi_func() #Prints hi
hello_func() #Prints hello
#Notice that each of these functions remembers the values of their own msg variable
