T = int(input())
for i in range(T):
    total_cars = int(input())
    speeds = list(map(int,input().split()))
    count = 1
    for i in range(1,len(speeds)):
        if speeds[i] < speeds[0]:
            speeds[0] = speeds[i]
            count+=1
    print(count)