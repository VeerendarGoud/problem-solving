
def tribonacci(n: int) -> int:
    a,b,c = 0,1,1
    if n==0: return a
    if n==1: return b
    if n==2: return c
    
    for i in range(3,n+1):
        tmp=a+b+c
        a,b,c = b,c,tmp
    return c

def tribonacci(n: int) -> int:
    
    dp=dict()
    dp[0]=0
    dp[1]=1
    dp[2]=1
    
    def recur(n):
        if n in dp:
            return dp[n]
        dp[n] = recur(n-1)+recur(n-2)+recur(n-3)
        return dp[n]
    
    return recur(n)