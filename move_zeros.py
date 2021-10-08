'''
 * @file   DoublyLinkedList.py
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Armin Zare Zadeh, ali.a.zarezadeh@gmail.com
 * @date   20 Jun 2020
 * @version 0.1
 * @brief   A doubly linked list implementation.
'''

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    le = len(nums)
    end = le-1
    start = 0
    
    for i in range(le):
        
        
        if nums[i] == 0:
            print(i) 
            
            del nums[i]
            nums.insert(-1,0)      

    return nums

nums = [0,0,1]
print(moveZeroes(nums))