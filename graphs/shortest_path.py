import sys

def find_shortest_path(edges,source,dest):

    visited = set(source)

    min_path = None

    graph = build_graph(edges)

    print(graph)

    queue = [[source,0]]

    while len(queue) > 0:

        current_ele,current_dist = queue.pop(0)

        #print(current_ele,current_dist)

        if current_ele == dest:

            # print(current_dist)

            # if min_path is None:
            #     min_path = current_dist
            # else:
            #     min_path = min(min_path,current_dist)

            return current_dist

        for ele in graph[current_ele]:
            if ele not in visited:
                queue.append([ele,current_dist+1])
                visited.add(ele)

    # if min_path is not None:
    #     return current_dist

    return -1

    

def build_graph(edges):

    graph = {}

    for edge in edges:
        [a,b] = edge

        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['x','v'],
    ['w','v'],
]
source = 'w'
dest = 'z'
print(find_shortest_path(edges,source,dest)) # 2