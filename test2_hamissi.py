from queue import Queue
import numpy as np
import random
import os
import os.path
import matplotlib.pyplot as plt


def make_random_path(nbr_vertices,length):
    l = random.sample(range(0,nbr_vertices), length)
    print(l)
    return l
    '''
    for i in range(len(l)):
        if i!=len(l)-1:
            print(str(l[i]) + " " + str(l[i+1]))'''

#make_random_path(4,4)

def make_uniform_pattern(nbr_length_per_instance,nbr_instance,nbr_vertices):
    f = open("/home/fatemeh/Bureau/Stage/data/unifrom_pattern_"+str(nbr_length_per_instance)+"_"+ str(nbr_instance) + ".txt", "w")
    for j in range(0,nbr_instance):
        l = make_random_path(nbr_vertices,nbr_length_per_instance)
        for i in range(len(l)):
            if i!=len(l)-1:
                f.write(str(j) + " " + str(l[i]) + " " + str(l[i+1]))
                f.write("\n")
    f.close()
    return f


def make_binary_tree_form_arbogen(trees,n,file_name):
    f2 = open(file_name, "w")
    for fname in trees:
        f = open(fname, "r")
        fi = f.readline()
        fi = f.readline()
        i = 0
        while fi[0]==" ":
            fi = f.readline()
            i=i+1
        line = fi.split()
        last = line[2]
        last1 = last[:len(last)-1]
        f2.write(str(trees.index(fname)) + " " + str(line[0]) + " " + str(last1))
        f2.write("\n") 
        for j in range(0,i-2):
            fi = f.readline()
            line = fi.split()
            last = line[2]
            last1 = last[:len(last)-1]
            f2.write(str(trees.index(fname)) + " " + str(line[0]) + " " + str(last1))
            f2.write("\n")    
    
    f2.close()
    return f2

def generate_random_target_stream(number_of_vertex_per_instance,number_of_instances,file_name):
    l = []
    for i in range(number_of_instances+1):
        while True:  
            os.system('arbogen -o ~/Bureau/Stage/arbre'+ str(number_of_vertex_per_instance) + '_' + str(i) +' -otype dot ~/arbogen-master/examples/binary'+str(number_of_vertex_per_instance)+'.spec')
            f =  'arbre' + str(number_of_vertex_per_instance) + '_' + str(i) + '.dot'
            if(os.path.exists(os.path.join('/home/fatemeh/Bureau/Stage/', f))):  
               break  
        l.append('/home/fatemeh/Bureau/Stage/'+f)
    r = make_binary_tree_form_arbogen(l,number_of_instances,file_name)
    print("Done ! target stream created.")
    return r

generate_random_target_stream(1000,100,"/home/fatemeh/Bureau/Stage/target_100inst_1000vert.txt")
# make_binary_tree_form_arbogen(["/home/fatemeh/Bureau/Stage/arbre.dot"],1,"target_1000.txt")
#print(os.path.exists(os.path.join('/home/fatemeh/Bureau/Stage/', 'arbre' + str(1000) + '_' + str(0) + '.dot')))    

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

"""
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
    
    #The case we have found a path the not yet associated way
    if g_to_unique_path == None:
        g_to_paths = bfs(g,testing[0])
        g_to_unique_path = max((x) for x in g_to_paths)
    
    for i in range(len(potential_path)):
        if (g_to_unique_path[i] not in mapi):
            mapi[g_to_unique_path[i]] = potential_path[i]
    return mapi

#print(find_pattern([[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]],[[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]],[0,1,2,3],{}))

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

def make_random_path(nbr_vertices,length):
    l = random.sample(range(0,nbr_vertices), length)
    print(l)
    return l
    '''
    for i in range(len(l)):
        if i!=len(l)-1:
            print(str(l[i]) + " " + str(l[i+1]))'''

#make_random_path(4,4)

def make_uniform_pattern(nbr_length_per_instance,nbr_instance,nbr_vertices):
    f = open("/home/fatemeh/Bureau/Stage/data/unifrom_pattern_"+str(nbr_length_per_instance)+"_"+ str(nbr_instance) + ".txt", "w")
    for j in range(0,nbr_instance):
        l = make_random_path(nbr_vertices,nbr_length_per_instance)
        for i in range(len(l)):
            if i!=len(l)-1:
                f.write(str(j) + " " + str(l[i]) + " " + str(l[i+1]))
                f.write("\n")
    f.close()
    return f


def make_random_tree(nbr_vertices,nbr_vertices_per_tree):
    l = random.sample(range(0,nbr_vertices), nbr_vertices_per_tree)
    l2 = []
    print(l)
    for i in range(len(l)):
        l2.append(random.randint(1,2))
    
    print(l2)
    not_choosed = l[:]
    print("not choosed " + str(not_choosed))

    l3 = []

    i = 0
    first = random.choice(not_choosed)
    index = not_choosed.index(first)
    not_choosed.remove(first)
    nbr_children = l2[index]
    while len(not_choosed) > 0:
        if len(not_choosed) == 1:
            return l3
        elif len(not_choosed) == 2:
            nbr_children = 0
        if nbr_children == 0:
            choosed = random.choice(not_choosed)
            index = not_choosed.index(choosed)
            not_choosed.remove(choosed)
            print(str(first) + " " + str(choosed))
            l3.append([first,choosed])
            first = choosed
            nbr_children = l2[index]
        elif nbr_children == 1 :
            choosed = random.choice(not_choosed)
            index = not_choosed.index(choosed)
            not_choosed.remove(choosed)
            print(str(first) + " " + str(choosed))
            l3.append([first,choosed])
            first = choosed
            nbr_children = l2[index]
        elif nbr_children == 2 :
            choosed1 = random.choice(not_choosed)
            index1 = not_choosed.index(choosed1)
            not_choosed.remove(choosed1)

            choosed2 = random.choice(not_choosed)
            index2 = not_choosed.index(choosed2)
            not_choosed.remove(choosed2)

            print(str(first) + " " + str(choosed1))
            print(str(first) + " " + str(choosed2))


            l3.append([first,choosed1])
            l3.append([first,choosed2])

            if random.randint(0,1) == 0:
                first = choosed1
                nbr_children = l2[index1]
            else:
                first = choosed2
                nbr_children = l2[index2]
        print(not_choosed)
    return l3

#print(make_random_tree(10,7))

'''
    for i in range(len(l)):
        if i!=len(l)-1:
            print(str(l[i]) + " " + str(l[i+1]))'''


def make_uniform_target(nbr_vertices_per_instance,nbr_instance,nbr_vertices):
    f = open("/home/fatemeh/Bureau/Stage/data/uniform_target_"+str(nbr_instance)+"_"+ str(nbr_vertices_per_instance) +".txt", "w")
    for j in range(0,nbr_instance):
        l = make_random_tree(nbr_vertices,nbr_vertices_per_instance)
        print("je suis la liste" + str(l))
        for i in l:
            f.write(str(j) + " " + str(i[0]) + " " + str(i[1]))
            f.write("\n")
            
    f.close()
    return f

#make_uniform_pattern(20,5,30)
#make_uniform_target(40,10,100)

#example_target = to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/example_target.txt"),4)
#example_pattern = to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/example_pattern.txt"),4)

#target_binh =  to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/graphbinh.txt"),2)
#pattern_binh =  to_list_of_matrices(file_to_graphs("/home/fatemeh/Bureau/Stage/patternBinh.txt"),2)

#print(KMPSearch(pattern_binh,target_binh,[0,1]))
#print(KMPSearch(example_pattern,example_target,[0,1,2,3]))"""