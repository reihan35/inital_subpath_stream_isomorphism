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
    i=0
    while (queue.empty() == False):
        i+=1
        x  = queue.get()
        print(x)
        print("breath = " + str(i))
        print(neighbours(x,G))
        for w in neighbours(x,G):
            if visited[w] == 0: 
                queue.put(w)             
                visited[w] = 1
    return x 

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
                    return (-1,p)
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
            if visited[adjacent]==0:
                if (has_children_yet==False):
                    i = i + 1 
                    has_children_yet = True
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    
    return node

print( bfs([0,1,2,3,4,5,6,7],[[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,0,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,1,0],[0,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,0]],9, 0,[]))


#print(BFS([0,1,2,3,4,5,6,7],[[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,0,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,1,0],[0,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,0]],0)) 