#Generators
#Advantage:
#If you need to access your data only once, using generators will allow you to decrease your
#memory usage (because data are generated on the spot) and your program will run faster.

#Disadvantage:
#if you need to access your data several times, you are still going to decrease your memory
#usage but your program will be slower since the generator and the data need to be generated each time. 

#This is the normal way we take in a list of numbers and produce a list of the squares
def square_nums_normal(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result
#Calling the normal square generating function
my_nums = square_nums_normal([1,2,3,4,5])
print(my_nums) #Returns [1,4,9,16,25]

#This is the way to do it with a generator
#This creates a generator object that does not calculate the values until we ask for them
def square_nums_generator(nums):
    for i in nums:
        yield i*i

my_nums = square_nums_generator([1,2,3,4,5])
print(my_nums) #This returns <generator object square_nums_generator at 0x03364E10>
#In order to access the results, we can do:

print(next(my_nums)) #Gives us 1
print(next(my_nums)) #Gives us 4
print(next(my_nums)) #Gives us 9
print(next(my_nums)) #Gives us 16
print(next(my_nums)) #Gives us 25
#print(next(my_nums)) Gives us an error

#Alternatively, we can call them with a for loop
#This won't work right now because the 5 iterations have already been called above
'''
for numbers in my_nums:
    print(numbers)
'''

#A list comprehension would have done it as so:
square_nums = [x*x for x in [1,2,3,4,5]]
print(square_nums) #Gives us [1,4,9,16,25]

#Changing it to a generator is as simple as changing the square brackets to round ones
square_nums = (x*x for x in [1,2,3,4,5])
print(square_nums) #This gives us the generator object again

#To change a generator to a list, we can do the following
#But this loses the advantages in performance again
list_nums = list(square_nums)

#Using a 2nd generator on a generator will replace the original
lst1 = (x*x for x in [1,2,3])   # [1, 4, 9]
lst2 = (x+x for x in lst1)  # [2, 8, 18]
for i in lst2: #Prints out [2, 8, 18]
    print(i)
for i in lst1: #Doesn't print out anything
    print(i)
