from collections import Counter

for i in range(int(input())):
    
    s = input()
    if len(s) % 2!=0:
        l = int(abs(len(s)/2))
        r = int(abs(len(s)/2))+1
        
    else:
        l = int(abs(len(s)/2))
        r = int(abs(len(s)/2))
        
    if Counter(s[:l])==Counter(s[r:]):
        print('YES')
    else:
        print('NO')
