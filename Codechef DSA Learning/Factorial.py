T = int(input())
for i in range(T):
    N = int(input())
    no_of_trailing_zeros = 0
    while (N>=1):
        N = N//5
        no_of_trailing_zeros += N
    print(no_of_trailing_zeros)
    
