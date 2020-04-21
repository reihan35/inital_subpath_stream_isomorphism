from queue import Queue
def neighbours(node,E):
    n = []
    for i in range(0,len(E[node])):
        if E[node][i]==1:
            n.append(i)
    return n

def bfs(gprim,start):
    visited = []
    for x in range(0,len(gprim)):
        visited.append(0)
    queue = []
    all_paths = []

    queue.append([start])
    all_paths.append([start])

    i=0
    while queue:
        path = queue.pop(0)
        node = path[-1]
        visited[node]=1
        for adjacent in neighbours(node,gprim):
            print(adjacent)
            if visited[adjacent]==0:
                i = i + 1 
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                all_paths.append(new_path)
    
    return all_paths

def bfs2(gprim,start):
    visited = []
    for x in range(0,len(gprim)):
        visited.append(0)
    queue = []
    all_paths = []

    queue.append([start])
    all_paths.append([start])
    
    i=0
    while queue:
        path = queue.pop(0)
        node = path[-1]
        visited[node]=1
        for adjacent in neighbours(node,gprim):
            print(adjacent)
            if visited[adjacent]==0:
                i = i + 1 
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                all_paths.append(new_path)
    
    return all_paths