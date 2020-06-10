import itertools
from queue import Queue
import collections

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

def creat_all_mappings(E,Eprim,t):
    list_mappings = []
    for i in range (0,len(E)):
        list_mappings.append(creat_all_mappings_for_single_graph(Eprim[t+i],E[i]))
    
    return  list(itertools.product(*list_mappings))
    #return list_mappings

def get_key(val,my_dict): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def mergeDict(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    for key in dict3.keys():
        if key in dict2.keys() and key in dict1.keys():
            if  dict1[key] != dict3[key]:
                print("je rentre la")
                return -1
        values = dict3.values()
        duplicates = [item for item, count in collections.Counter(values).items() if count > 1]
        print("duplicaaaaatessss" + str(duplicates))
        if duplicates != []:
            #print("bah non je rentre la")
            return -1

    return dict3

#print(mergeDict({0:2, 1:1, 2:0},{2:0, 4:5, 3:5}))
#print(mergeDict(mergeDict({0:2, 1:1, 2:0},{2:0, 4:5, 3:6}),{4:5, 5:7}))


def is_valid(mapping):
    dict3 = mapping[0].copy()
    for dict2 in enumerate(mapping):
        print(dict3)
        dict3 = mergeDict(dict3, dict2[1])
    
    return dict3
        
#print(is_valid(({0: 2, 1: 1, 2: 0}, {2: 0, 3: 6, 4: 5}, {4: 5, 5: 7})))

def creat_all_mappings_for_single_graph(gprim,g):
    testing_gprim = []
    testing_g = []
    list_mappis = []
    paths_in_gprim = []

    for i in range(len(gprim)):
        for j in range(len(gprim)) :
            if gprim[i][j] == 1 and i not in testing_gprim:
                testing_gprim.append(i)
    
    for i in range(len(g)):
        for j in range(len(g)) :
            if g[i][j] == 1 and i not in testing_g:
                testing_g.append(i)
                if len(neighbours(i,g))==1:
                    start = i
                    print("j'entre ici" + str(start))


    g_to_paths = bfs(g,start)
    g_to_path_side_1 = max((x) for x in g_to_paths)
    print("pattern")
    print("le voilaaaa" + str(g_to_paths))
    print(g_to_path_side_1)

    
    for v in testing_gprim:
       for chemin in (bfs(gprim,v)):
            paths_in_gprim.append(chemin)
    
    potential_paths = []
    for p in paths_in_gprim:
        if len(p) == len(testing_g):
            potential_paths.append(p)
    
    print(potential_paths)
    for p in potential_paths:
        mapi = dict()
        for i in range(len(p)):
            mapi[g_to_path_side_1[i]] = p[i]
        list_mappis.append(mapi)
    
    return list_mappis

#print(creat_all_mappings_for_single_graph([[0,1,1,0,0],[1,0,0,1,1],[1,0,0,0,0],[0,1,0,0,0],[0,1,0,0,0]],[[0,1,0],[1,0,1],[0,1,0]]))

example_target = to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/sample_target.txt"),9)
example_pattern = to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/sample_pattern.txt"),6)

#print(creat_all_mappings(example_pattern,example_target,0))

def naive_algo(E,Eprim):
    #for t in range (0,len(Eprim)):
    mappings = creat_all_mappings(E,Eprim,0)
    print("C'EST LE DEBUT ICI")
    print(mappings[8])
    i = 0
    for m in mappings:
        if(i==8):
            print("YEEEEEEESSSSS on est arrive au bon truc !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(m)
        i=i+1
        print("ON VA ANALYSER" + str(m))
        merged = is_valid(m)
        print("oui je suis la" + str(merged))
        if merged!=-1:
            return (merged,0)
    return -1

print(naive_algo(example_pattern,example_target))