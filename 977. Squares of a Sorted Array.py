
def sortedSquares(nums):

    i = 0
    j = len(nums)-1
    k = len(nums)-1
    
    squared_array = [0]*(j+1)

    while i <= j:

        #print(i,j,k)
        #print(squared_array)

        if abs(nums[i]) > abs(nums[j]):
            squared_array[k] = nums[i]*nums[i]
            i+=1
            k-=1
        elif abs(nums[i]) < abs(nums[j]):
            squared_array[k] = nums[j]*nums[j]
            j-=1
            k-=1
        else:
            squared_array[k] = nums[j]*nums[j]
            j-=1
            k-=1
    return squared_array
                
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
nums = [-5,-3,-2,-1]
print(sortedSquares(nums))