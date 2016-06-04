#List comprehensions is an easier and more readable way to create a list

nums = [1,2,3,4,5,6,7,8,9,10]

#####  Example 1   ######
#I want 'n' for each 'n' in nums

#Traditional for loop method
my_list = []
for n in nums:
    my_list.append(n)
print(my_list) #[1,2,3,4,5,6,7,8,9,10]
#Using list comprehension
my_list = [n for n in nums]
print(my_list) #[1,2,3,4,5,6,7,8,9,10]


##### Example 2 #####
#I want n**2 for each 'n' in nums

#Traditional for loop method
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)
#List comprehension method
my_list = [n*n for n in nums]
print(my_list)
#Using map and lambda
my_list = map(lambda n: n*n, nums) #Not readable unless you know lambda+map
print(list(my_list))


##### Example 3 #####
#I want n for each n in nums if n is even

#Traditional for loop method
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)
#List comprehension method
my_list = [n for n in nums if n%2 == 0]
#Using a filter and lambda
my_list = filter(lambda n: n%2 == 0, nums) #Not readable
print(list(my_list))


##### Example 4 #####
#I want a (letter, number) par for each letter "abcd" and each number "0123"

#For loops method
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)
#List comprehension method
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)





    
