#Dictionary Comprehensions

names = ['Nathan', 'Steven', 'Daniel', 'Christie', 'Emily']
jobs = ['Chef', 'Doctor', 'Lawyer', 'Idol', 'None']

#If the names and jobs are the same in length, we use zip
#This creates a list of tuples where the 0th index of the first list is matched
#with the 0th index of the second list
paired = zip(names, jobs)
print(list(paired))
#If you have one list that is longer than the other, it stops at the last element
#of the shorter list. I.E it doesn't pair up any extra elements

#If we want a dictionary of {'name', 'jobs'} for each name, hero in paired

#For loop method
my_dict = {}
for name, job in zip(names, jobs):
    my_dict[name] = job
print(my_dict)

#Dictionary comprehension method
my_dict = {name:job for name,job in zip(names,jobs)}
print(my_dict)
#Gives us
#{'Christie': 'Idol', 'Nathan': 'Chef', 'Steven': 'Doctor', 'Emily': 'None', 'Daniel': 'Lawyer'}

#If we didnt want Daniel in the list, we can add an if statement
my_dict = {name:job for name,job in zip(names,jobs) if name != 'Daniel'}
print(my_dict)
#Gives us
#{'Nathan': 'Chef', 'Steven': 'Doctor', 'Emily': 'None', 'Christie': 'Idol'}
