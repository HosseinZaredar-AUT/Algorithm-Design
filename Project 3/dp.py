c = open("./cost.txt","r")
c = c.readlines()
cost = []
temp = 0
for i in range(len(c)):  
    string = c[i]
    string = list(map(int,string.split()))
    temp = len(string)+1
    string = [0, *string]
    cost.append(string)
cost.insert(0,[0]*temp)

f = open("./relocationCost.txt","r")
f = f.readlines()
relocationCost = []
for i in range(len(f)):  
    string = f[i]
    string = list(map(int,string.split()))
    temp = len(string)+1
    string = [0,*string]
    relocationCost.append(string)
relocationCost.insert(0,[0]*temp)

n = len(cost[0]) -1
k = len(cost) -1

dp = [[0 for i in range(n+1)] for j in range(k+1)]
trace = [[0 for i in range(n+1)] for j in range(k+1)]

for i in range(1,k+1):
    dp[i][1] = cost[i][1]
    
for j in range(2, n+1):
    for i in range(1, k+1):
        mini = 0
        for m in range(1,k+1):
            if mini ==0 or mini > (dp[m][j-1] +relocationCost[m][i]):
                mini = dp[m][j-1] +relocationCost[m][i]
                dp[i][j] = dp[m][j-1] +relocationCost[m][i]
                trace[i][j] = m
        dp[i][j] += cost[i][j]
        
mini,num = 0,0  
for i in range(1,k+1):
    if mini == 0 or mini > dp[i][n]:
        mini = dp[i][n]
        num = i
lis = [num]
print(mini)
for i in range(n,1,-1):
    lis.append(trace[num][i])
    num = trace[num][i]
for i in range(len(lis)-1,-1,-1):
    print(lis[i], end=" ")