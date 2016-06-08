import matplotlib.pyplot as plt

#Setting the x and y values
x = [1,2,3]
y = [1,2,3]
x2 =[1,2,3]
y2 = [4,5,6]
#Creating a graph
plt.plot(x,y, label = 'Line 1')
plt.plot(x2,y2, label = "Line 2")
#Creating the titles
plt.xlabel('Plot Number')
plt.ylabel('Y variable')
plt.title('Title\nSystems Monitoring')
#Legend to distinguish between lines
plt.legend()
plt.show()
