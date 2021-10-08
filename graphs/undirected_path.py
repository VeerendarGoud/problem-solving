def has_path(graph,source,dest,visited=None):

    if visited is None:
        visited = set()
    if source in visited:
        return False
    else:
        visited.add(source)

    if source == dest:
        return True

    for nigh in graph[source]:
        result  = has_path(graph,nigh,dest,visited)
        if result:
            return True

    return False



    

def build_graph(edges):

    graph = dict()

    for pair in edges:

        [a,b] = pair

        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

        
edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n'],
]

source = 'i'
dest = 'k'

graph = build_graph(edges)

print(has_path(graph,source,dest))