def bubble_sort(customList):
    
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j],customList[j+1] = customList[j+1],customList[j]

    print(customList)


#bubble_sort([2,1,7,6,5,3,4,9,8])
#[1,2,3,4,5,6,7,8,9]

# Time Complexity O(n**2)
# Space Complexity O(1)

def selection_sort(customList):
    for i in range(len(customList)):                          # O(n)
        min_index = i
        for j in range(i+1, len(customList)):                 # O(n)
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i],customList[min_index] = customList[min_index],customList[i]
    print(customList)

#selection_sort([2,1,7,6,5,3,4,9,8])

# Time Complexity O(n**2)
# Space Complexity O(1)

def insertion_sort(customList):

    for i in range(1,len(customList)):
        key = customList[i]
        j = i-1

        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -=1
        customList[j+1] = key
    print(customList)

insertion_sort([2,1,7,6,5,3,4,9,8])

# Time Complexity O(n**2)
# Space Complexity O(1)
import math 

def bucket_sort(customList):
    number_of_bucket = round(math.sqrt(len(customList)))
    max_value = max(customList)
    arr = []

    for i in range(number_of_bucket):
        arr.append([])

    for j in customList:
        index_b = math.ceil(j*number_of_bucket/max_value)
        arr[index_b-1].append(j)

    for i in range(number_of_bucket):
        arr[i] = insertion_sort(arr) ### O(n**2)

    k = 0

    for i in ragne(number_of_bucket):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

# Time Complexity O(n**2)
# Space Complexity O(1)

def merge(customList, l,m,r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)
    