#Set comprehension
#Set is a list with all unique values
#Sets use {} not []


#For loop method
nums = [1,1,2,2,2,2,3,3,4,4,4,5]
my_set = set()
for n in nums:
    my_set.add(n) #set.add() is like append for lists
print(my_set)

#Set comprehension method
#As long as you already declared my_set = set(), you can do the following
my_set = {n for n in nums}
print(my_set)
