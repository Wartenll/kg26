from itertools import pairwise

val= ('8', '0', '8', '1', '2', '8')
for i in range (len(val)-1):
    if int (val[i]) % 2 == 0 and int (val[i+1]) % 2 == 0:

        print(val[i])

