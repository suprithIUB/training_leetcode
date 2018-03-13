def connected_comps_adjacency_matrix(graph):
    visited = set()
    components = 0
    for row in range(0,len(graph)):
        #for col in range(0, len(graph)):
        if(row not in visited):
            dfs(graph, row, visited)
            components += 1

    return components

def dfs(graph, current_node, visited):
    stack = list()
    stack.append(current_node)
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        for j in range(0, len(graph)):
            if graph[vertex][j] and j not in visited:
                stack.append(j)
                print("{0} --- {1}".format(vertex+1,j+1))
    return


if __name__ == "__main__":
    graph = [
            [0,1,0,0,1,0],
            [1,0,1,0,1,0],
            [0,1,0,1,0,0],
            [0,0,1,0,1,1],
            [1,1,0,1,0,0],
            [0,0,0,1,0,0]
            ]
    from pprint import pprint
    pprint(graph)
    pprint(connected_comps_adjacency_matrix(graph))

    graph = [
            [1,1,0,0,0,0],
            [1,1,1,0,0,0],
            [0,1,1,0,0,0],
            [0,0,0,1,1,0],
            [0,0,0,1,1,0],
            [0,0,0,0,0,1]
            ]

    pprint(graph)
    pprint(connected_comps_adjacency_matrix(graph))

