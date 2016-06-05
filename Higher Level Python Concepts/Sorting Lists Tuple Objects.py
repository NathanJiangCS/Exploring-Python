#Examples of sorting various objects


'Lists'
li = [1,4,5,6,12,3,8,9,10]

##### Sorting lists in ascending order #####
#Sorted version of li. It creates a new list as the original list li is unchanged
s_li = sorted(li)

#To sort the original li without creating a new list, we can use
li.sort()
#this sorts the list in place and returns none

##### Sorting lists in descending order #####
#We can do the same thing as above using sorted and pass in a reversed parameter
s_li = sorted(li, reverse=True)
li.sort(reverse=True)

##### Sorting lists based on special parameters #####
li = [-6,-5,-3,1,2,9]
#Sort list based on the absolute values

#In order to this, we can insert a key parameter
s_li = sorted(li, key=abs) #abs is the absolute value function.
#This runs each element through the absolute value function and then sorts them

#We can also do it for objects such as the following
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},{})'.format(self.name, self.age, self.salary)
    
e1 = Employee('Nathan', 100, 100)
e2 = Employee('John', 24, 60000)
e3 = Employee('Crystal', 22, 1000000)

employees = [e1,e2,e3]

s_employees = sorted(employees) #Sorting them without a key will result in an error
#We need to tell the function how to sort it

#By writing a custom function and pass it as the key, we can sort it
#This sorts it by name
def e_sort(emp):
    return emp.name

#When we state the function we are using as a key, we don't include parameters ()
#This is because if we do, we would be calling the function instead
s_employees = sorted(employees, key=e_sort)

#We can still pass in reverse=True parameter
s_employees = sorted(employees, key=e_sort, reverse=True)

#Alternatively, if we are working with attributes such as the employee class
#We can use attrgetter
from operator import attrgetter
#Then we can replace the key with attrgetter('attribute')
s_employees = sorted(employees, key=attrgetter('salary'))

print s_employees


'Tuples'
tu = (1,4,5,6,12,3,8,9,10)

#Tuples dont have a tuple.sort() method
#We have to use the sorted function
s_tu = sorted(tu) #This returns a sorted list of the values contained in the tuple


'Dictionaries'
di = {'name': 'Nathan', 'job': 'programming', 'age':None, 'stan':'Twice'}
#Once again, dictionaries don't have a dictionary.sort() method
#By using the sorted function, by default it sorts the keys
s_di = sorted(di)
print s_di #This returns ['age','job','name','stan']
           #in other words, a sorted list of the keys

