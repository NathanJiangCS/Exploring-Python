#think of a namedtuple as a more readable version of a normal tuple
#look at this example to see what this means


#This allows us to use namedtuples
from collections import namedtuple

#This normal tuple represents our color in RGB value. 
color = (55,123, 255)
#To print the red value
print color[0]
#But when other people come and look at this code, it is hard for them to tell
#that the system we are using is RGB. It could be hue saturation and light

#To make it more readable we can use a dictionary
color = {'red':55, 'green':123, 'blue':255}
print color['red']
#A dictionary is mutable while a tuple is immutable
#Also, dictonaries require more typing

#A namedtuple is a comprimise between a tuple and a dictionary. It provides the
#readability of a dictionary and functions as a tuple

#This is how we initiate a namedtuple
#in the brackets we have the name of our tuple followed by the name of the values
Color = namedtuple('Color', ['red','green','blue'])
#This is how we can assign values to our namedtuple
color = Color(55,123,255)
#If we want to be explicit in assigning the values for maximum readability
color = Color(red=55,green=123,blue=255)

#To print red, we can do either
print color[0]
print color.red #This is a lot more readable than a regular tuple

#To make another color, we can just do
white = Color(255,255,255)
print white.blue
