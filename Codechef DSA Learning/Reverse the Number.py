# T = int(input())
# num = []
# for i in range(T):
#     num.append(input())
# for k in num:
#     print(k[::-1])
    
T = int(input())
num = [input() for i in range(T)]
for i in num:
    print(int(i[::-1]))
    
    