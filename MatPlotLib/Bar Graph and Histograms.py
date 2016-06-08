import matplotlib.pyplot as plt
from random import randint

# #Bar Graph
# #Setting up x and y values

# x = [2,4,6,8,10]
# y = [6,7,4,6,5]
# x2 = [1,3,5,7,9]
# y2 = [4,3,6,5,2]

# #Creating the bar graph

# plt.bar(x, y, label="Bar 1", color="cyan")
# plt.bar(x2, y2, label="Bar 2", color="red")

#Histogram
age = [randint(20,100) for x in xrange(30)]
ids = [x for x in xrange(30)]

#Groups
bins = [0,10,20,30,40,50,60,70,80,90]

#Creating a histogram
#Y becomes the frequency of the age groups
plt.hist(age, bins, histtype='bar', rwidth=0.8)
#Axis
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')
#Creating a legend to display
#plt.legend()
#Showing the graph
plt.show()