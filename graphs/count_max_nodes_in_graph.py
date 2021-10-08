def count_connected_max_nodes(graph):
    visited = set()
    max_count  = 0

    for node in graph:
        current_count = count_nodes(graph,node,visited)
        print(current_count)
        if max_count < current_count:
            max_count = current_count
    return max_count 

def count_nodes(graph,node,visited):
    count = 0

    if node in visited:
        return 0
    else:
        visited.add(node)
        count +=1

    for current in graph[node]:
        # if explore(graph,current,visited):
        #     return True
        count += count_nodes(graph,current,visited)

    return count



components = {
    0:[8,1,5],
    1:[0],
    5:[8],
    8:[5],
    2:[3,4],
    3:[2,4],
    4:[2,3]
}

print(count_connected_max_nodes(components))