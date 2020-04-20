from queue import Queue
def neighbours(node,E):
    n = []
    for i in range(0,len(E[node])):
        if E[node][i]==1:
            n.append(i)
    return n

def bfs(V,Eprim,n, start,markedEprim):
    visited = []
    for x in range(0,len(V)):
        visited.append(0)
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    i=0
    while queue:
        print("i = " + str(i)) 
        print(queue)
        if(i==n):
            for p in queue:
                if p not in markedEprim:
                    return (-1,p,i)
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        visited[node]=1
        print(path)
        print(node)
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        has_children_yet=False
        for adjacent in neighbours(node,Eprim):
            print(adjacent)
            if visited[adjacent]==0:
                if (has_children_yet==False):
                    i = i + 1 
                    has_children_yet = True
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    
    return (node,-1,i)

#print( bfs([0,1,2,3,4,5,6,7],[[0,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0],[0,1,0,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,1,0],[0,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,0]],3, 3,[3,2,5,6]))


def find_pattern(n,Eprim,Vprim,markedEprim):
    w = Vprim[0]
    (u,p,dist) = bfs(Vprim,Eprim,n,w,markedEprim)
    #If we have not found a path of the desired length
    if (p == -1):
        (v,p,dist) = bfs(Vprim,Eprim,n,u,markedEprim)
        if (p!=-1):
            markedEprim.append(p)
        else :
            if (dist >= n):
                i = 1
                while (p==-1 or i<len(Vprim)):
                    i = i + 1
                    if (Vprim[i]!=u):
                        (x,p) = bfs(Vprim,Eprim,n,Vprim[i],markedEprim)
                if (p!=-1):
                    markedEprim.append(p)
            else :
                return (-1,-1)
    else:
        markedEprim.append(p)

    return (p,markedEprim)

#The input is a path stream
def preprocessing(V,E,T,Vprim,Eprim,Tprim) : 
    P = []
    pi = []
    for t in T : 
        P.append(len(E[t]))
    
    pi[0] = -1
    k = -1
    i = 0
    for i in range(0,len(Tprim)):
        while k<=0 and P[k+1] != P[i]:
            k = pi[k]
            pi[i] = k + 1
    
    return pi,P

def path_stream_matching (V,E,T,Vprim,Eprim,Tprim):
    (pi,P) = preprocessing(V,E,T,Vprim,Eprim,Tprim)
    k = 0
    R = []
    T_r = []
    markedEprim = []
    for t in Tprim : 
        (pattern,markedEprim) = find_pattern(P[k+1],Eprim,Vprim,markedEprim)
        while k>=0 and pattern != -1:
            k = pi[k]
            k = k + 1
            if k == len(T) :
                k = pi[k]
                T_r.append(t)
                R.append((V,pattern,T_r))
                T_r = []
    return R

#print(find_pattern(3,[[0,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0],[0,1,0,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,1,0],[0,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,0]],[0,1,2,3,4,5,6,7],[[3,2,5,6]]))

def preprocessing(V,E,T,Vprim,Eprim,Tprim):
    pi = []
    pi.append(-1)
    k = 1
    i = 1
    for i in range (len(Tprim)):
        while k <= 0 and graphsequal(E[k+1] != E[i]):
            k=pi[k]
            pi[i] = k+1
    return pi
