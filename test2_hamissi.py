def file_to_graph(file):
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
            edges.append(data)
            print(edges)
        else:
            #graphs.append(edges)
            print("avant" + str(graphs))
            edges = []
            edges.append(data)
            graphs.append(edges)
            print("apres" + str(graphs))
        a = data[0]
    return graphs

print(file_to_graph("/home/fatemeh/Bureau/Stage/graph.txt"))