with open(r'.\files\17_9786.txt') as file:
    data = (int(i) for i in file)
max_25 = max(i for i in data if i % 100 == 25)
ans=[]
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(num1)) == 4
    u2 =





    #https://chat.deepseek.com/a/chat/s/d91111f6-174f-4990-a79e-ad03c71b3a71
    #https://kompege.ru/variant?kim=25166329