from string import ascii_uppercase
with open(r'../files/24_9791.txt') as file:
    data = file.readline()

for i in ascii_uppercase[6:]:
    data = data.replace(i, ' ')
data = data.split()