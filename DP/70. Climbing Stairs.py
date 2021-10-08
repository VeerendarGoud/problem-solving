
def climbing_stairs(n,visited=None):

    # base case
    if n == 1:
        return 1
    elif n ==2:
        return 2
    elif n <= 0:
        return 0

    if visited is None:
        visited = dict()

    count = 0

    if n in visited:
        return visited[n]
        
    # recursive case
    count += climbing_stairs(n-1,visited) + climbing_stairs(n-2,visited)

    visited[n] = count

    print(visited)
    
    return count

    # if n <= 0: return 0
    # if n == 1: return 1
    # if n == 2: return 2
    # dp = [0] * (n + 1)
    # dp[1], dp[2] = 1, 2
    # for i in range(3, n + 1):
    #     dp[i] = dp[i-1] + dp[i-2]
    # return dp[n]


print(climbing_stairs(5))


# Please upvote if you like any of the solutions.

# Approach 1:

# def climbStairs(self, n: int) -> int:
# 	# climbStairs(n) = climbStairs(n-2)+climbStairs(n-1)
# 	# So, start at [1, 1] (climbStairs(0)=climbStairs(1)=1)
# 	# and keep moving window of solutions forward n-1 times to get to solution
# 	return reduce(lambda a, _: [a[1], a[0]+a[1]], range(n-1), [1, 1])[1]
# Equivalent to this solution(less memory than 98%):

# def climbStairs(self, n: int) -> int:
# 	# Inital at n=0, n=1
# 	curr = [1, 1]
# 	# Move window of solutions forward
# 	for _ in range(n-1):
# 		curr[0], curr[1] = curr[1], curr[0]+curr[1]

# 	return curr[1]
# Approach 2: Mathematical, Faster than 95% of solutions.
# Idea: This problem is the same as finding the nth fibonacci number. Use the closed-form approximation for calculating the nth fibonacci number.

# def climbStairs(self, n: int) -> int:

# 	root_5 = sqrt(5)
# 	return round((((1 + root_5) / 2)**(n+1))/root_5)