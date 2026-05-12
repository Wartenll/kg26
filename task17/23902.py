with open(r'.\files\17_4597.txt') as file:
    data = [int(i) for i in file]
    a=[int(i) for i in file]
ans=[]
for i in range(len(a)-2):
    x,y,z=a[i],a[i+1],a[i+2]
    if sum(str(n)[0]==str(n)[-1] for n in (x,y,z))==1 and sum(1000<=n<=9999 and (n//100)%10==2 for n in (x,y,z))==2:
        ans.append(max(x,y,z))
print(len(ans),sum(ans))