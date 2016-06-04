import sys

#This writes in the error text to shell
sys.stderr.write('test\n')
sys.stderr.flush()

#Writes it in normal text to the shell 
sys.stdout.write('test\n')

