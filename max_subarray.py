### brute force
'''
def maxSubArray(nums) -> int:
        
    max_sum = nums[0]
    
    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        
        for j in range(i+1,len(nums)+1):

            print(i,j,nums[i:j])

            loop_sum = sum(nums[i:j])
            
            if loop_sum > max_sum:
                max_sum = loop_sum
            
            
    return max_sum

print(maxSubArray([-2,-1])) #-1
print(maxSubArray([5, 4, -1, 7, 8]))#23
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))#6

'''

## kandane's algoritham

def max_sub_array(nums):

    if len(nums) == 1:
        return nums[0]

    max_sum = nums[0]
    max_sub_array = [nums[0]]

    current_sum = nums[0]
    current_sub_array = [nums[0]]

    for i in range(1,len(nums)):

        if current_sum + nums[i] > nums[i]:
            current_sub_array.append(nums[i])
            current_sum += nums[i]
            if max_sum < current_sum:
                max_sum = current_sum
                max_sub_array = current_sub_array.copy()
        else:
            current_sub_array = [nums[i]]
            current_sum = nums[i]
            if max_sum < current_sum:
                max_sum = current_sum
                max_sub_array = current_sub_array.copy()


    return max_sum

def maxSubArray2(self, nums) -> int:

    max_sum = nums[0]

    current_sum = nums[0]

    for i in range(1,len(nums)):

        current_sum = max(nums[i],current_sum+nums[i])
            
        max_sum = max(current_sum, max_sum)
            

    return max_sum

def maxSubArray(nums) -> int:        
    maxarr = nums[0]
    currmax = 0 
    
    for i in range(len(nums)):
        currmax = currmax + nums[i]
        if maxarr < currmax:
            maxarr = currmax
        if currmax < 0:
            currmax = 0
    return maxarr
        

print(maxSubArray([-2,-1])) #-1
print(maxSubArray([5, 4, -1, 7, 8]))#23
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))#6