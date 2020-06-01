for i in range(int(input())):
    k, d0, d1 = map(int,input().split())
    num = [d0, d1, (d0 + d1) % 10]
    temp = d0+d1
    add = sum(num[:k])
    l=[]
    if k > 3:
        for i in range(4):
            l.append((temp*2) % 10)
            temp =(temp*2) % 10
        div, rem = divmod(k - 3, 4)
        add += sum(l) * div + sum(l[:rem])
    if add%3 == 0:
        print("YES")
    else:
        print("NO")

