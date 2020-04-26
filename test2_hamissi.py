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
        matrices.append(to_adjacency(graph,n-1))
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
        #print("path_to_match" + str(path_to_match))
        #print("c'est ce path la qu'on regarde" + str(path))
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
    #print("voici mapi" + str(mapi))
    no_associated = True
    testing = []
    g_to_unique_path = None
    for i in range(len(g)):
        for j in range(len(g)) :
            if g[i][j] == 1 and i not in testing:
                testing.append(i)
    
    for vertice in testing:
        if vertice in mapi :
            no_associated = False
            start = mapi[vertice]
            g_to_paths = bfs(g,vertice)
            g_to_unique_path = max((x) for x in g_to_paths)
            (path1,path2)=shrink_paths(g_to_paths,len(testing))
            #print("path1 vaut " + str(path1))
            #print("path2 vaut " + str(path2))
            break

    n = len(testing)
    testing2 = []
    #print("testing vaut " + str(testing))
    #print("n vaut " + str(n))
    for i in range(len(gprim)):
        for j in range(len(gprim)) :
            if gprim[i][j] == 1 and i not in testing2:
                testing2.append(i)
    
    if mapi == [] or no_associated :
        w = testing2[0]
        paths = bfs(gprim,w)
        print(paths)
        (potential_path,maxList) = path_of_size(paths,n)
        print("JE SUIS RENTREE ICI + potential" + str(potential_path))
        #print("maxList" + str(maxList))
        if potential_path == -1:
            u = maxList[len(maxList)-1]
            paths = bfs(gprim,u)
            (potential_path,maxList) = path_of_size(paths,n)
            v = maxList[len(maxList)-1]
            if potential_path == -1:
                if len(maxList) < n:
                    return {}
                else:
                    i = 1
                    while potential_path == -1:
                        i=i+1
                        if(testing2[i]!=u or testing2[i]!=v):
                            paths = bfs(gprim,testing2[i])
                            (potential_path,maxList) = path_of_size(paths,n)
    else:
        #print("g_to_unique_path" + str(g_to_unique_path))
        paths = bfs(gprim,start)
        potential_path1 = find_specific_path_using_bfs(paths,path1,mapi)
        potential_path = find_specific_path_using_bfs(paths,path2,mapi)
        print("je suis Laaaaaaaaaaaaaaa " + str(potential_path1))
        print("je suis Laaaaaaaaaaaaaaa " + str(potential_path))

        if potential_path == [] and potential_path1 == []:
            return {}
        for i in range (len(potential_path1)):
            if (g_to_unique_path[i] not in mapi):
                mapi[g_to_unique_path[i]] = potential_path1[i]
    
    if g_to_unique_path == None:
        g_to_paths = bfs(g,testing[0])
        g_to_unique_path = max((x) for x in g_to_paths)
    
    for i in range(len(potential_path)):
        if (g_to_unique_path[i] not in mapi):
            mapi[g_to_unique_path[i]] = potential_path[i]
    return mapi

#print(find_pattern([[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]],[[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]],[0,1,2,3],{}))

def preprocessing(E,T):
    pi = []
    
    for i in range (0,T+1):
        pi.append(-1)
    
    k = -1
    for i in range (1,T+1):
        #print("k " + str(k))
        #print("i " + str(i))
        #print("E[k+1]" + str(E[k+1]))
        #print("E[i]" + str(E[i]))
        #print("Pi avant " + str(pi))
        while k >= 0 and graphsequal(E[k+1],E[i]) == False:
            k=pi[k]
          #  print("dans la boucle = " + str(k))
        k = k+1
        pi[i] = k
        #print("Pi apres " + str(pi))

    return pi

        
def path_stream_matching(E,T,Eprim,Tprim,Vprim):
    pi = preprocessing(E,T)
    #pi = [0,0]
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!PI EGALE" + str(pi))
    k = 0
    i = 0
    result = []
    mapi = dict()
    for t in range(1,Tprim):
        print("BOUCLEEEEEE" + str(t))
        print("E[" + str(k+1) + "] " + str(E[k+1]))
        print("Eprim[" + str(t) + "] " + str(Eprim[t]))
        mapi = find_pattern(Eprim[t],E[k+1],Vprim,mapi)
        print("mapi vaut " + str(mapi))
        while k>=0 and mapi == {}:
            k = pi[k]
            print(k)
        k = k + 1
        print("k VAUUUTT " + str(k))
        if k == T :
            print(" !!!!!!!! K et hope je rentre ici" + str(k))
            k = pi[k-1]
            result.append((t-T,mapi))
    return result



def put(P):
    P2 =[]
    P2.append(-1)
    for i in range(0, len(P)) :
        P2.append(P[i])
    return P2


#print(example_pattern)
#print(preprocessing(put(example_pattern),7))

#print(path_stream_matching(put(example_pattern),7,put(example_target),18,[0,1,2,3]))


def computeLPSArray(E, T, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < T: 
        if graphsequal(E[i],E[len]): 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1

def KMPSearch(E, Eprim,Vprim): 
    M = len(E) 
    N = len(Eprim) 
    result = []
    mapi = dict()
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(E, M, lps) 
  
    i = 0 # index for txt[] 
    while i < N: 
        mapi = find_pattern(Eprim[i],E[j],Vprim,mapi)
        if  mapi!={}: 
            i += 1
            j += 1
  
        if j == M: 
            result.append(((i-j),mapi))
            print(str(Eprim[i-j]))
            print "Found pattern at index " + str(i-j) 
            j = lps[j-1] 

  
        # mismatch after j matches 
        elif i < N and E[j] != Eprim[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    
    return result


example_target = to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/example_target.txt"),4)
example_pattern = to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/example_pattern.txt"),4)


print(KMPSearch(example_pattern,example_target,[0,1,2,3]))