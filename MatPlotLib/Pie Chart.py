import matplotlib.pyplot as plt 

#Total days
days = [1,2,3,4,5]

#Events that occur during parts of the day
a = [7,8,6,11,7]
b = [2,3,4,3,2]
c = [7,8,7,2,2]
d = [8,5,7,8,13]

slices = [7,2,2,13]
activities = ['a','b','c','d']
cols = ['r','b','c','m']
#Slices is the sizes, labels is the names of each slice, explode brings out a piece at the specified index
#autopct is displaying the percentage of each slice
plt.pie(slices, 
		labels=activities, 
		colors=cols, 
		startangle=90, 
		shadow=True, 
		explode=(0,0.1,0,0),
		autopct='%1.1f%%')
#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Title')
plt.legend()
plt.show()