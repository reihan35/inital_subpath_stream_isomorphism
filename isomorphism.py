from queue import Queue

def neighbours(node,E):
    n = []
    for i in range(0,len(E[node])):
        if E[node][i]==1:
            n.append(i)
    return n

def BFS (V,G,s):    
    visited = []
    for x in range(0,len(V)):
        visited.append(0)
    queue = Queue() 
    queue.put(s)  
    visited[s] = 1
    while (queue.empty() == False):
        x  = queue.get()
        print(x)
        print(neighbours(x,G))
        for w in neighbours(x,G):
            if visited[w] == 0: 
                queue.put(w)             
                visited[w] = 1
    return x


#The input is a path stream
def preprocessing(V,E,T) : 
    p = []
    pi = []
    for t in T : 
        p.append(len(E[t]))
    
    pi[0] = -1
    k = -1
    i = 0
    for i in range(0,len(T)):
        while k<=0 and p[k+1] != p[i]:
            k = pi[k]
            pi[i] = k + 1
    return pi


def find_pattern(n,E_prim,V,marked):
    if has_pattern(n,E_prim,V):
        pathes = pathes_of_size(n,E_prim)
        for p in pathes:
            if marked[p] == 0 :
                marked = mark(p)
                return (p,marked)
    return

def has_pattern(n,E_prim,V):
    w = V[0]
    u = BFS(V,E_prim,w)
    v = BFS(V,E_prim,u)

    return distance(u,v) > n


def path_stream_matching (V,E,T,V_p,E_p,T_p,pi,p):
    k = 0
    i = 0
    R = []
    T_r = []
    E_r = []
    marked_E_p = E_p
    for t in T_p : 
        (pattern,marked_E_p) = find_pattern(p[k+1],marked_E_p,V)
        while k>=0 and pattern != None:
            k = pi[k]
            k = k + 1
            if k == T :
                k = pi[k]
                T_r.append(t)
                R.append((V,pattern,T_r))
                T_r = []
                E_r = []
                marked_E_p = E_p
    return R
