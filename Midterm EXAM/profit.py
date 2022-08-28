n = int(input())
c = int(input())
p = int(input())
d = int(input())
s = int(input())
if d>n :
    profit = n*(p-c)
    op_cost = (d-n)*(p-c)
    total_profit = profit-op_cost
else :
    profit = d*(p-c)
    loss = (n-d)*(c-s)
    total_profit = profit-loss
print(total_profit)