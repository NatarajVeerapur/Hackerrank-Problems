

def getMoneySpent(keyboards, drives, b):
    x=0
    y=[-1]
    for i in range(0,n):
        for j in range(0,m):
            x=keyboards[i]+drives[j]
            if x<=b and x>y[0]:
                y.insert(0,x)
    
    
    return y[0]    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
