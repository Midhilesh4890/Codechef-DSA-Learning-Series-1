T = int(input())
for i in range(T):
    activities, origin = (input().split())
    
    total = 0
    
    for i in range(int(activities)):
        activity_type = list(input().split())
        
        if activity_type[0]== 'CONTEST_WON':
            total +=300
            if int(activity_type[1])<=20:
                total+=(20-int(activity_type[1]))
        
        if activity_type[0]== 'TOP_CONTRIBUTOR':
            total +=300
            
        if activity_type[0]== 'BUG_FOUND':
            total += int(activity_type[1])
            
        if activity_type[0]== 'CONTEST_HOSTED':
            total +=50
            
    if origin == 'INDIAN':
        print(total // 200)
    
    if origin == 'NON_INDIAN':
        print(total // 400)
    
        
    
