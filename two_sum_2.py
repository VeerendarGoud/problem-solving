def twoSum(numbers, target):
        
    diff_dict = dict({})
    
    for i in range(len(numbers)):
        
        diff = target-numbers[i]
        
        if diff in diff_dict:
            return [diff_dict[diff],i]
        else:
            diff_dict[numbers[i]] = i
            
    #return diff_dict


numbers = [2,7,0,10]
target = 9
print(twoSum(numbers, target))