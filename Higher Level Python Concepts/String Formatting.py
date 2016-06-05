#String formatting
#Advanced operations for Dicts, Lists, and numbers

person = {'name':'Nathan', 'age':100}

#######################
#Sentence using string concatenation
sentence = "My name is " + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print sentence
#This is not readable as you have to open and close strings
#You also have to remember to place spaces

#######################
#Sentence using %s
sentence = "My name is %s and I am %s years old." % (person['name'], person['age'])
print sentence

#######################
#Sentence using .format
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])

#You can also explicitly number your placeholders
#By doing this, your value at the specified index will replace that placeholder
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])

#For example, we don't have to type the text value twice when using this formatting
tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print sentence

#We can also specify specific fields from the placeholders themselves
#Before we were doing this
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
#We can also do this. This method also works for a list or a tuple
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print sentence

#We can also access attributes in a similar way
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('Jack',33)

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print sentence

#We can also pass in keyword arguments
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jen',age=30)

#This means we can unpack a dictionary and format the sentence in a similar way
#By unpacking the dictionary, it fills in the keyword arguments for us
person = {'name':'Jen', 'age', 30}
sentence = 'My name is {name} and I am {age} years old.'.format(**person)

#By adding a colon in our placeholders, we can add formatting
#For example, lets say we wanted to make all of our values 2 digits by padding a zero
for i in range(1,11):
    sentence = 'The value is {:02}'.format(i)
    print sentence
#This gives us 01, 02, 03, 04 ... 10, 11. We can change {:02} to {:03} and it gives us
#001, 002, 003 .... 010, 011

#This is how we format decimal places
pi = 3.14152965
sentence = 'Pi is equal to {:.2f}'.format(pi)
#This rounds pi to 2 decimal places 3.14

#We can also chain formatting. For example, if we wanted to add commas to make a large
#number more readable but also have the large number rounded to 2 decimal places
sentence = '1MB is equal to {:,.2f} bytes'.format(1000**2)
#See how we chained , which inserts the commas to make it more readable with .2f
