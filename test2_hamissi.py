def file_to_graphs(file):
    f = open(file, "r")
    a = -1
    edges = []
    graphs = []
    for line in f : 
        #print("I am")
        data = line.split()
        #print(data)
        #print("data[0]", data[0])
        #print( "a", a)
        #print(data[0] == a)
        if data[0] == a:
            edges.append(data[1:])
            #print(edges)
        else:
            #graphs.append(edges)
            #print("avant" + str(graphs))
            edges = []
            edges.append(data[1:])
            graphs.append(edges)
            #print("apres" + str(graphs))
        a = data[0]
    return graphs

#print(file_to_graphs("/home/fatemeh/Bureau/Stage/graph.txt"))

def to_adjacency(edges,n):
    #print(edges)
    #size = int(edges[len(edges)-1][1])
    size = n
    res = [ [ 0 for i in range(size+1) ] for j in range(size+1) ] 
    #print(size)
    #print(res)
    for edge in edges:
        #print(edge)
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

print(to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/target.txt"),5))

def graphsequal(g1,g2):
    for i in range (len(g1)) :
        for j in range (len(g1)) :
            if g1[i][j] != g2[i][j] :
                return False
    return True

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

def path_of_size(paths,n):
    maxList = max((x) for x in paths) 
    for path in paths:
        if len(path)>=n:
            return (path,maxList[len(maxList)-1])
    return (null,maxList)

def find_pattern(t,gprim,Vprim,mapi,tprim):
    no_associated = True
    testing = []
    for i in range(len(gprim)):
        for j in range(len(gprim)) :
            if gprim[i][j] == 1:
                testing.append(i,j)
    
    for vertice in testing:
        if (mapi[vertice]==-1):
            no_associated = False
            (path1,path2)=shrink_paths(bfs(gprim,vertice),len(testing))
    
    n = len(testing)

    if mapi == [] or no_associated :
        w = v[0]
        paths = bfs(gprim,w)
        (potential_path,maxList) = path_of_size(paths,n)
        if potential_path == null:
            u = maxList[len(maxList)-1]
            paths = bfs(gprim,u)
            (potential_path,maxList) = path_of_size(paths,n)
            v = maxList[len(maxList)-1]
            if potential_path == null:
                if len(maxList) < n:
                    return -1
                else:
                    i = 1
                    while potential_path == null:
                        i=i+1
                        if(v[i]!=u or v[i]!=v):
                            paths = bfs(gprim,v[i])
                            (potential_path,maxList) = path_of_size(paths,n)
    else:

    return potential_path

        
def path_stream_matching(E,T,Eprim,Tprim):
    pi = preprocessing(E,T)
    k = 0
    i = 0
    result = []
    mapi = []
    for t in range(0,Tprim):
        mapi = find_pattern()
        while k>=0 and map != []:
            k = pi[k]
            k = k + 1
            if k == T :
                k = pi[k]
                result.append(t,mapi)
    return result