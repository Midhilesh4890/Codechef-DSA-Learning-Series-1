T = int(input())
for i in range(T):
    G = int(input())
    for i in range(G):
        I,N,Q = map(int,input().split())
        
        if I==1:
            no_of_heads = N//2
            no_of_tails = N - N//2
            
        if I==2:
            no_of_tails = N//2
            no_of_heads = N - N//2
            
        if Q==1:
            print(no_of_heads)
        else:
            print(no_of_tails)
            
