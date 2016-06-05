#Else statement at the end of loops
#Think about the else statement at the end of a loop as a "no-break"
my_list = [1,2,3,4,5]

####### For Loops #######
#Will run the else statement
for i in my_list:
    print i
else:
    print 'Hit the for/else statement'

#Will not run the else statement because a break is hit during the for loop
for i in my_list:
    print i
    if i==3:
        break
else:
    print 'Hit the for/else statement'

####### While Loops #######
#Will run the else statment
i = 1
while i <= 5:
    print i
    i += 1
else:
    print 'Hit the while/else statment'

#Will not run the else statment
i = 1
while i <= 5:
    print i
    i += 1
    if i == 3:
        break
else:
    print 'Hit the while/else statment'


###### Practical Example ######
def find_index(to_search, target):
    for i, value in enumerate(to_search): #i is index and value is the value at the index    
        print i, value
        if value == target:
            break
    else:
        return -1
    return i

my_list = ['Nathan', 'John', 'Jack']
#This returns the index of 2
index_location = find_index(my_list, 'Jack')
#This returns the index of -1 (i.e not found)
index_location = find_index(my_list, 'Sam')
