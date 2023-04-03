num = int (input("enter your number:"))
decTobinNum=""
while (num>0):
    
    if (num%2 == 0):
        decTobinNum='0'+decTobinNum
    else:
        decTobinNum='1'+decTobinNum
    num=num//2

print(decTobinNum)    
