'''
 * @file   704_binary_search.py
 * @author veerendar konda, veerendar2888@gmail.com
 *         
 * @date   24 Sep 2021
 * @version 0.1
 * @brief   Binary Search Tree (BST) data structure implementation.
 * This file contains an implementation of a Binary Search Tree (BST) Any comparable data is allowed
 * within this tree (numbers, strings, comparable Objects, etc...). Supported operations include
 * adding, removing, height, and containment checks. Furthermore, multiple tree traversal Iterators
 * are provided including: 1) Preorder traversal 2) Inorder traversal 3) Postorder traversal 4)
 * Levelorder traversal
'''


'''
def search(nums,target,s,e):

    print(s,e)

    if e >= s:

        mid = (s+e)//2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return search(nums,target,s,mid-1)
        else:
            return search(nums,target,mid+1,e)
    else:
        return -1
        

A= [-1,0,3,5,9,12]

print(search(A,2,0,len(A)-1))

'''

def search(nums,target,s,e):

    print(s,e)

    if e >= s:

        mid = (s+e)//2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return search(nums,target,s,mid-1)
        else:
            return search(nums,target,mid+1,e)
    else:
        return s
        

#A= [1,3,5,6]
A = [0]
print(search(A,0,0,len(A)-1))