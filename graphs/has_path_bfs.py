def has_path(graph,source,destination):

    if source == destination:
        return True
    
    for ele in graph[source]:
        result = has_path(graph,ele,destination)
        if result:
            return True
    return False

def has_path_bfs(graph,source,destination):

    queue = [source]

    while len(queue) > 0:
        current_ele = queue.pop(0)
        if current_ele == destination:
            return True
        queue.extend(graph[current_ele])

    return False


graph = {
    'a':['c','b'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}
source = 'a'
destination = 'z'
#print(has_path(graph,source,destination))
print(has_path_bfs(graph,source,destination))