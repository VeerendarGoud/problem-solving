#
def getWays(n, c):
    table = [0]*(n+1)   
    table[0] = 1
    count = 0
    for i in range(n):
        if table[0] != 0:
            for num in c:
                if i+num <= n:
                    table[i+num] += table[i] 
        #print(table)

    return table[n]

#print(getWays(4, [1,2,3]))#4
#print(getWays(10, [2,5,3,6])) #5
print(getWays(5,[1,2,5]))
# 1111
#112
#211
#13
#31
#121
#22

## recursion

'''
def getWays(n,c,memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    count = 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    for num in c:
        r = n-num
        result = getWays(r,c,memo)
        if result:
            count += result
    memo[n] = count
    return count

'''
'''
def getWays(n, c):
    n_perms = [1]+[0]*n
    for coin in c:
        for i in range(coin, n+1):
            n_perms[i] += n_perms[i-coin]
        print(n_perms)
    return n_perms


#print(getWays(4, [1,2,3]))#4
#print(getWays(10, [2,5,3,6])) #5
print(getWays(3, [8,3,1,2])) #5

'''
