# Created by Veerendar Konda 8 oct 2021
# # binary tree data structure

# class binarySearchTree:
#     def __init__(self) -> None:
#         self.val = Val
#         self.left = None
#         self.right = None

#     def insert(self,val):
#         # check if there is no root
#         if (self.value == None):
#             self.val = val

class binaryTree:
    def __init__(self,data=None) -> None:
        self.val = data
        self.left = None
        self.right = None
    def __repr__(self) -> str:
        return str(self.val)

    def insert_1(self,val):
        # check if thereis no root
        if self.val == None:
            self.val = val
        # check where to insert
        else:
            # check for duplicate then stop and return
            if self.val == val : return "no duplicates allowed in binary search tree."

            # check if value to be inserted < currentNode's value
            if (val < self.val):

                # check if there is a left node to current node if true then recurse
                if (self.val):
                    self.left.insert(val)
                # insert where left of current node when 
                else:
                    self.left = binaryTree(val)
            # same steps as above here the condition we check is value to be inserted > current node value
            else:
                if (self.right):
                    self.right.insert(val)
                else: self.right = binaryTree(val)


    def breadthFirstSearch(self):
        currentNode = self
        bfs_list = []
        queue = []
        queue.insert(0,currentNode)

        while (len(queue) >0):
            currentNode = queue.pop()
            bfs_list.append(currentNode.val)
            if (currentNode.left):
                queue.insert(0,currentNode.left)
            if (currentNode.right):
                queue.insert(0,currentNode.right)
        return bfs_list

    def depthFirstSearch_InOrder(self):
        return self.traverseInOrder([])
    def depthFirstSearch_PreOrder(self):
        return self.traversePreOrder([])
    def depthFirstSearch_PostOrder(self):
        return self.traversePostOrder([])

    def traversePreOrder(self,lst):
        lst.append(self.val)
        if (self.left):
            self.left.traversePreOrder(lst)
        if (self.right):
            self.right.traversePreOrder(lst)
        return lst
    def traverseInOrder(self,lst):
        if (self.left):
            self.left.traverseInOrder(lst)
        lst.append(self.val)
        if (self.right):
            self.right.traverseInOrder(lst)
        return lst
    def traversePostOrder(self,lst):
        if (self.left):
            self.left.traversePostOrder(lst)
        if (self.right):
            self.right.traversePostOrder(lst)
        lst.append(self.val)
        return lst

    def insert(self,val):
        # check if there is no root
        if self.val == None:
            self.val = val
        # check where to insert
        else:
            # check for duplicate then stop and return 
            if val == self.val:
                return 'no duplicates allowed in binary search tree'
            # check value to be inserted  < current node's value
            if (val < self.val):
                #check if there is a left node to current node if true then recurse
                if (self.left):
                    self.left.insert(val)
                # insert where left of currentNode when currentNode.left=None
                else:
                    self.left = binaryTree(val)
            else:
                if (self.right):
                    self.right.insert(val)
                else:
                    self.right = binaryTree(val)

    def find_node_and_its_parents(self,val,parent=None):

        # returning the node and its parent so we can delete the node and reconstruct the tree from its parent
        if val == self.val:
            return self,parent
        if val < self.val:
            if self.left:
                return self.left.find_node_and_its_parents(val,self)
            else:
                return 'Not found'
        else:
            if self.right:
                return self.right.find_node_and_its_parents(val,self)
            else:
                return 'Not found'

    # deleting the node means we have to rearrange some part of the tree

    def delete(self,val):
        # check if the value we want to delete is in the tree
        if self.find_node_and_its_parents(val) == "Not found": return "Node is not in tree."
        # we get the node we want to delete and its parent-node from find node and its parents menthod
        deleteing_node, parent_node = self.find_node_and_its_parents(val)
        # check how may children nodes does the node we are going to delete have by traversePreOrder from the deleteing_node
        nodes_effected = deleteing_node.traversePreOrder([])
        # if len(nodes_effected)==1 means, the node to be deleted doesn't have any children
        # so we can just check from its parent node the position(left or right) of node we want to delete
        # and point the position to 'None' i.e node is deleted
        if len(nodes_effected) == 1:
            if (parent_node.left.val == deleteing_node.val): parent_node.left = None
            else: parent_node.right = None
            return "Successfully deleted"
        # if len(nodes_effected) > 1 which means the node we are going to delete has 'children',
        # so the tree must be rearranged from the deleteing_node
        else:
            # if the node we want to delete doesn't have any parent means the node to be deleted is 'root' node
            if (parent_node == None):
                nodes_effected.remove(deleteing_node.val)
                # make the 'root' nodee i.e self value,left,right to None,
                # this means we need to implement a new tree again without the delted node
                self.left = None
                self.right = None
                self.val = None
                # contruction of new tree
                for node in nodes_effected:
                    self.insert(node)
                return "Successfully deleted"
            
            # if the node we want to delete has a parent
            # traverse from parent_node
            nodes_effected = parent_node.traversePreOrder([])
            # deleting the node
            if (parent_node.left == deleteing_node): parent_node.left = None
            else: parent_node.right = None
            # removeing the parent_node, deleteing_node and inserting the nodes_effected in the tree
            nodes_effected.remove(deleteing_node.val)
            nodes_effected.remove(parent_node.val)
            for node in nodes_effected:
                self.insert(node)

        return 'Successfully deleted'



bst = binaryTree()
bst.insert(7)
bst.insert(4)
bst.insert(9)
bst.insert(0)
bst.insert(5)
bst.insert(8)
bst.insert(13)


print('IN order: ',bst.depthFirstSearch_InOrder()) # useful in sorting the tree in ascending order
print('PRE order:' ,bst.depthFirstSearch_PreOrder()) # pre order is useful in reconstructing a tree
print('POST order:', bst.depthFirstSearch_PostOrder()) # useful in finding the leaf nodes

print(bst.find_node_and_its_parents(5))

# print(bst.delete(5))
# print(bst.delete(9))
print(bst.delete(7))

#after deleting
print('IN order: ',bst.depthFirstSearch_InOrder())






# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return []
#     nodes = []
#     nodes.append (rootNode.val)
#     nodes.extend(preOrderTraversal(rootNode.left))
#     nodes.extend(preOrderTraversal(rootNode.right))

#     return nodes
        

# btree = binaryTree("Dirnks")
# btree.left = binaryTree("Hot")
# btree.right  = binaryTree("Cold")
# nodes = preOrderTraversal(btree)
# print(nodes)
# print(btree.breadthFirstSearch())
# print(btree.depthFirstSearch_InOrder())
# print(btree.depthFirstSearch_PreOrder())
# print(btree.depthFirstSearch_PostOrder())

# #print(btree)