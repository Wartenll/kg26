with open(r'..\files\24_4602.txt') as file:
    data = file.readline()
data = data.replace('BA', '*')
data = data.replace('CA', '*')
data = data.replace('DA', '*')
data = data.replace('BO', '*')
data = data.replace('CO', '*')
data = data.replace('DO', '*')
for i in set(data):
    if i != '*':
        data= data.replace(i,' ')
data = data.split()
print(len(max(data, key=len)))