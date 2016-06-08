#Showing parts of a whole
import matplotlib.pyplot as plt 

#Total days
days = [1,2,3,4,5]

#Events that occur during parts of the day
a = [7,8,6,11,7]
b = [2,3,4,3,2]
c = [7,8,7,2,2]
d = [8,5,7,8,13]

#Creating the stackplot
#The first value is your x
#Then its followed by the rest of your events that will stack up in the specified order
plt.stackplot(days, a,b,c,d, colors=['cyan','m','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')

#No labels in stackplot
#plt.legend()

plt.show()