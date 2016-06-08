import matplotlib.pyplot as plt 

#Data to plot
x = [1,2,3,4,5,6,7,8]
y = [4,2,6,4,5,2,5,1]
#Marker is the dot that we see
#size is the size of the marker
plt.scatter(x,y, label='Scatter Plot', color = 'cyan', marker='*', s=100)

#Creating labels
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')

plt.legend()
plt.show()