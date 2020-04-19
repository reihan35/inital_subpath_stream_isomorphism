def file_to_graphs(file):
    f = open(file, "r")
    a = -1
    edges = []
    graphs = []
    for line in f : 
        print("I am")
        data = line.split()
        print(data)
        print("data[0]", data[0])
        print( "a", a)
        print(data[0] == a)
        if data[0] == a:
            edges.append(data[1:])
            print(edges)
        else:
            #graphs.append(edges)
            print("avant" + str(graphs))
            edges = []
            edges.append(data[1:])
            graphs.append(edges)
            print("apres" + str(graphs))
        a = data[0]
    return graphs

#print(file_to_graphs("/home/fatemeh/Bureau/Stage/graph.txt"))

def to_adjacency(edges):
    print(edges)
    size = int(edges[len(edges)-1][1])
    res = [ [ 0 for i in range(size+1) ] for j in range(size+1) ] 
    print(size)
    print(res)
    for edge in edges:
        print(edge)
        res[int(edge[0])][int(edge[1])] = 1 
        res[int(edge[1])][int(edge[0])] = 1
    return res

#print(to_adjacency([ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5],
#[3,8], [4,5], [4,9], [7,8], [7,9] ]))

def to_list_of_matrices(graphs):
    matrices = []
    for graph in graphs:
        matrices.append(to_adjacency(graph))
    return matrices

print(to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/graph.txt")))
