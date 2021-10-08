
def best_sum(targetSum, numbers):
    table = [None] * (targetSum+1)
    table[0] = []
    for i in range(targetSum+1):
        if table[i] is not None:
            for num in numbers:
                if i+num <= targetSum:
                    #print(table)
                    combination = [*table[i], num]
                    if table[i+num] is None or len(combination) < len(table[i+num]):
                        table[i+num] = combination
                    
    return table[targetSum]

print(best_sum(7, [2, 3]))
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(7, [2, 4]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(300, [7, 14]))