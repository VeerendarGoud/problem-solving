def rotate(nums,k):

    le = len(nums)
    if k > le:
        k = k%le

    nums.extend(nums[:(le-k)])
    del nums[:(le-k)]

    return nums

nums = [-1,-100,3,99]
k = 2
print(rotate(nums,k))
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))
nums = [1,2]
k = 3
print(rotate(nums,k))
