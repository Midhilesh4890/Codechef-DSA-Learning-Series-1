T = int(input())
customer_budget = []
for i in range(T):
    customer_budget.append(int(input()))
customer_budget.sort()
max_revenue = 0
for i in range(T):
    max_revenue = max(max_revenue,customer_budget[i]*T)
    T -= 1
print(max_revenue)
