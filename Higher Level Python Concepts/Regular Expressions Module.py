'''
Identifiers:

\d (any number)
\D (anything but a number)
\s (space)
\S (anything but a space)
\w (any character)
\W (anything but a character)
.  (any character, except for a newline)
\b (the whitespace around words)
\. (a period)

Modifiers:
{1,3} (excpecting 1-3 of something. E.g. \d{1-3} is numbers 1-3 in length)
+ (Match 1 or more)
? (Match 0 or 1)
* (Match 0 or more)
$ (Match the end of a string)
^ (Matching the beginning of a string)
| (Matches either or)
[] (range or variance. E.g [1-5a-q-A-Z] means searching for anything within those ranges)
{x} (expecting "x" amount)

Whitespace Characters:
\n (newline)
\s (space)
\e (escape)
\t (tab)
\f (form feed)
\r (return)

'''
import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. '''

#First argument is the regular expression, second is the string to be searched
#\d indicates we are looking for a number
#{1,3} means that it is 1-3 in length
ages = re.findall(r'\d{1,3}', exampleString)

#The [A-Z] searches for any uppercase A-Z
#Unlike the example at the top, having closed brackets side by side indicate we are
#looking for this after that. Therefore, we are looking for lowercase a-z after our upper case
#A-Z. The * represents we are looking for 0 or more of these lowercase characters
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)
#Another thing we can do is search for variations of a word
#Quantitative vs Quantatative
#We can just search for Quant[ia]tative

exampleLine = 'prices xom 91.43-91.44/vr50-50.01/s 7.23-7.24'
#Looking for stock names such as xom, vr, and s.
#First it is 1-3 characters long; therefore we use \w{1,3}
#Then it could be followed by either 1 space or no space. WE use \s?
#Then we look for 1-2 digits/ We use \d{1,2}
#Then we have a decimal which isn't required. We use \.?
#Then we have more digits, either 0-2. \d{0,2}
#They all have the dash. We write -
#Then more digits. \d{1,2}
#Then a decimal which is not required. We use \.?
#Then a final number. \d{0,2}
#Together it is \w{1,3}\s?\d{1,2}\.?\d{0,2}-\d{1,2}\.?\d{0,2}
regEx = re.findall(r'\w{1,3}\s?\d{1,2}\.?\d{0,2}-\d{1,2}\.?\d{0,2}',exampleLine)
print(regEx)
#


