#Eval is shortform for evaluate
#Can't evaluate a definition
#Only can evaluate an expression
list_str = '[1,2,3,4,5]'
list_str = eval(list_str)
print(list_str)

#We can eval input such as print('hi') and we would see hi ouputted
#However, we cannot eval statements such as z=5. This is a definition
x = input('What code do you want to run: ')
y = eval(input('What code do you want to run: '))

print(y)

################################################
#Exec is shortform for execute
#Compiles and evaluates whatever you pass through it in string form
#Exec is dangerous

#This does not work because we are executing a list which doesn't make sense
list_str='[3,2,4]'
list_str=exec(list_str)
print(list_str)
#However, you can do things such as this (definitions)
#You can even define functions 
exec('list_str2 = [2,3,5]')
print(list_str2)
