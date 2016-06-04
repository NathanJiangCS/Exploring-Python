#Try and Except in Python 3
#Also includes some example of else and finally
#Use try and except blocks to handle sections of code that might result in error
#Always try to be specific when catching an error
import csv 

with open('sample.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #reads as a string
    dates = []
    colors = []
    for row in readCSV:
        date = row[0].strip()
        color = row[3].strip()

        dates.append(date)
        colors.append(color)
        
    #Tries a block of code and goes to except if there is an error
    try:
        whatColor = input('enter a color and ill give you the date ')
        #If/Else is an alternative solution here for Try/Except
        #if whatColor in colors:
        #else:
        
    #except Exception,e: for python 2
    except Exception as e:
        print(e)
        
    else: #Runs if try doesn't result in an error.
        coldex = colors.index(whatColor)
        print("The date is %s" % dates[coldex])
        print('Color is not found')

    finally: #Runs regardless if there is an exception or now
        print('Finally block")
              
    #Even if an error occurs, the program continues
    print('continuing')

#Exception is the most general. When handling exceptions, put the most general at the bottom
#Other types of exceptions include:
#FileNotFoundError
#NameError

#You can also raise your own exception
#if something:
#   raise Exception
