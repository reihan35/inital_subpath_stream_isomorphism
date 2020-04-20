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

#def find_pattern(t,gprim,Vprim,mapi,tprim):
 #   no_connected = True
 #   for a in range (len(gprim)):
  #      if ()
  #  if mapi == [] or no_connected 

def path_stream_matching(E,T,Eprim,Tprim):
    pi = preprocessing(E,T)
    k = 0
    i = 0
    result = []
    mapi = []
    for t in range(Tprim):
        mapi = find_pattern()
        while k>=0 and map != []:
            k = pi[k]
            k = k + 1
            if k == T :
                k = pi[k]
                result.append(t,mapi)
    return result