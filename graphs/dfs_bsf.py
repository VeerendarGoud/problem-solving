
def dfs(graph,start_ele):

    stack = [start_ele]

    while len(stack) > 0:

        current = stack.pop(-1)

        print(current)

        stack.extend(graph[current])

def dfs_recursive(graph,start_ele):

    print(start_ele)


    # we don't need base case in this senario.
    if len(graph[start_ele]) ==0:
        #print(start_ele)
        return 
    
    for ele in graph[start_ele]:
        
        dfs_recursive(graph,ele)
        


def bsf(graph,start_ele):

    queue = [start_ele]

    while len(queue)>0:
        current_ele = queue.pop(0)
        print(current_ele)
        queue.extend(graph[current_ele])

    

graph = {
    'a':['c','b'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

print(dfs(graph,'a'))

print(dfs_recursive(graph,'a'))

print(bsf(graph,'a'))


