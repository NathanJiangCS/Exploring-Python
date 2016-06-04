#CSV files are popular for storing data
#comma seperated variables
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

    whatColor = input('enter a color and ill give you the date ')
    coldex = colors.index(whatColor)

    print("The date is %s" % dates[coldex])
