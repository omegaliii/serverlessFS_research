from loggingos import *

print('with read')
print(open)
with open('myFile.txt') as f:
    print(f)
    print(f.read())

