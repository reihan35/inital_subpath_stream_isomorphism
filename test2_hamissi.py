from queue import Queue
def file_to_graphs(file):
    f = open(file, "r")
    a = -1
    edges = []
    graphs = []
    for line in f : 
        data = line.split()
        if data[0] == a:
            edges.append(data[1:])
        else:
            edges = []
            edges.append(data[1:])
            graphs.append(edges)
        a = data[0]
    return graphs

#print(file_to_graphs("/home/fatemeh/Bureau/Stage/graph.txt"))

def to_adjacency(edges,n):
    size = n
    res = [ [ 0 for i in range(size+1) ] for j in range(size+1) ] 
    for edge in edges:
        res[int(edge[0])][int(edge[1])] = 1 
        res[int(edge[1])][int(edge[0])] = 1
    return res

#print(to_adjacency([ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5],
#[3,8], [4,5], [4,9], [7,8], [7,9] ]))

def to_list_of_matrices(graphs,n):
    matrices = []
    for graph in graphs:
        matrices.append(to_adjacency(graph,n))
    return matrices

#print(to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/target.txt"),5))

def graphsequal(g1,g2):
    for i in range (len(g1)) :
        for j in range (len(g1)) :
            if g1[i][j] != g2[i][j] :
                return False
    return True

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
            #print(adjacent)
            if visited[adjacent]==0:
                i = i + 1 
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                all_paths.append(new_path)
    
    return all_paths

def preprocessing(E,T):
    pi = []
    pi.append(-1)
    k = -1
    for i in range (0,T):
        while k >= 0 and graphsequal(E[k+1],E[i]) == False:
            k=pi[k]
            pi[i] = k+1
    return pi

#print(preprocessing(to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/pattern.txt")),2,to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/target.txt")),5))
def shrink_paths(paths,n):
    maxList = max((x) for x in paths) 
    if len(maxList) != n :
        paths.remove(maxList)
        maxList2 = max((x) for x in paths)
    else:
        return (maxList,[])
    return (maxList,maxList2)

#print(shrink_paths([[1],[1,2,4],[1,2,3]],4))


def path_of_size(paths,n):
    maxList = max((x) for x in paths) 
    for path in paths:
        if len(path)>=n:
            return (path,maxList[len(maxList)-1])
    return (-1,maxList)

#print(path_of_size([[1],[1,2],[1,2,3,]],4))

def find_specific_path_using_bfs(paths,path_to_match,mapi):
    j = 0
    for path in paths:
        print("path_to_match" + str(path_to_match))
        print("c'est ce path la qu'on regarde" + str(path))
        if len(path)==len(path_to_match):
            #print("c'est ce path la qu'on regarde" + str(path))
            for i in range (0,len(path)):
                #print("je rentre ici")
                #print(path_to_match[i])
                #print(path[i])
                if (path_to_match[i] in mapi and mapi[path_to_match[i]] == path[i]):
                    j=j+1
                elif (path_to_match[i] not in mapi and path[i] not in mapi.values()):
                    #print("Bien sur que je comprends")
                    j = j+1

            if j == len(path):
                return path
            j = 0
    return []

#print(bfs([[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]],0))

#print(find_specific_path_using_bfs(bfs([[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]],0),[0,3],{0:0,1:1,2:2}))

def find_pattern(gprim,g,Vprim,mapi):
    no_associated = True
    testing = []
    for i in range(len(g)):
        for j in range(len(g)) :
            if g[i][j] == 1:
                testing.append(i)
    
    for vertice in testing:
        if vertice in mapi :
            no_associated = False
            start = mapi[vertice]
            g_to_paths = bfs(g,vertice)
            g_to_unique_path = max((x) for x in g_to_paths)
            (path1,path2)=shrink_paths(g_to_paths,len(testing))
            break

    n = len(testing)

    if mapi == [] or no_associated :
        w = Vprim[0]
        paths = bfs(gprim,w)
        (potential_path,maxList) = path_of_size(paths,n)
        if potential_path == -1:
            u = maxList[len(maxList)-1]
            paths = bfs(gprim,u)
            (potential_path,maxList) = path_of_size(paths,n)
            v = maxList[len(maxList)-1]
            if potential_path == -1:
                if len(maxList) < n:
                    return -1
                else:
                    i = 1
                    while potential_path == -1:
                        i=i+1
                        if(Vprim[i]!=u or Vprim[i]!=v):
                            paths = bfs(gprim,Vprim[i])
                            (potential_path,maxList) = path_of_size(paths,n)
    else:
        #print("g_to_unique_path" + str(g_to_unique_path))
        paths = bfs(gprim,start)
        potential_path1 = find_specific_path_using_bfs(paths,path1,mapi)
        potential_path = find_specific_path_using_bfs(paths,path2,mapi)
        
        for v in potential_path1:
            if (g_to_unique_path[i] not in mapi):
                mapi[g_to_unique_path[i]] = potential_path1[i]
    
    for v in potential_path:
        if (g_to_unique_path[i] not in mapi):
            mapi[g_to_unique_path[i]] = potential_path[i]
    return mapi

find_pattern([[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]],[[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]],[0,1,2,3],{0:0,1:1,2:2})

        
def path_stream_matching(E,T,V,Eprim,Tprim,Vprim):
    pi = preprocessing(E,T)
    k = 0
    i = 0
    result = []
    mapi = dict()
    for t in range(0,Tprim):
        mapi = find_pattern(Eprim[t],E[t],Vprim,mapi)
        while k>=0 and mapi != -1:
            k = pi[k]
            k = k + 1
            if k == T :
                k = pi[k]
                result.append(t,mapi)
    return result