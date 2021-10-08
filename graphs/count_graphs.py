def count_connected_components(graph):
    visited = set()
    count  = 0

    for node in graph:
        if explore(graph,node,visited):
            count += 1
    return count 

def explore(graph,node,visited):

    if node in visited:
        return False
    else:
        visited.add(node)

    for current in graph[node]:
        # if explore(graph,current,visited):
        #     return True
        explore(graph,current,visited)
    return True



components = {
    0:[8,1,5],
    1:[0],
    5:[8],
    8:[5],
    2:[3,4],
    3:[2,4],
    4:[2,3]
}

print(count_connected_components(components))
