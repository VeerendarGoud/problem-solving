import sys
 
 
# Function to find the maximum sublist sum using divide-and-conquer
def findMaximumSum(A, left, right):
 
    # If the list contains only one element
    if right == left:
        return A[left]
 
    # Find the middle element in the list
    mid = (left + right) // 2
 
    # Find maximum sublist sum for the left sublist,
    # including the middle element
    leftMax = -sys.maxsize
    sum = 0
    for i in range(mid, left - 1, -1):
        sum += A[i]
        if sum > leftMax:
            leftMax = sum
 
    # Find maximum sublist sum for the right sublist,
    # excluding the middle element
    rightMax = -sys.maxsize
    sum = 0        # reset sum to 0
 
    for i in range(mid + 1, right + 1):
        sum += A[i]
        if sum > rightMax:
            rightMax = sum
 
    # Recursively find the maximum sublist sum for the left
    # and right sublist, and take maximum
    maxLeftRight = max(findMaximumSum(A, left, mid), findMaximumSum(A, mid + 1, right))
 
    # return the maximum of the three
    return max(maxLeftRight, leftMax + rightMax)
 
 
if __name__ == '__main__':
 
    A = [2, -4, 1, 9, -6, 7, -3]
    
    print("The Maximum sum of the sublist is", findMaximumSum(A, 0, len(A) - 1))