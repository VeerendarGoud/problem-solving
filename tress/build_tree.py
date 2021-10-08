class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.left) + '--'+str(self.data) + '--'+str(self.right)

def add_nodes(root,arr,i,n):

    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        root.left = add_nodes(root.left,arr,2*i+1,n)
        root.right = add_nodes(root.left,arr,2*i+2,n)

    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def level_order(root):
    if root is not None:
        print(root.data,end= ' ')
        level_order(root.left)
        level_order(root.right)


arr = [1,2,4,5,3]
#arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
root = None

root = add_nodes(root,arr,0,len(arr))

#inorder(root)
level_order(root)