def preprocessing(P,m):
    pi = []
    if len(P) == 2 and P[0] == P[1]: 
        return [-1,0]
    
    for i in range (0,m):
        pi.append(-2)
    
    print(pi)
    k = -2
    for i in range (1,m):
        print("---- debut boucle " + str(i))
        print("k " + str(k))
        print("P[k+1]" + str(P[k+1]))
        print("P[i]" + str(P[i]))
        while(k >= -1 and P[k+1] != P[i]):
            print("---" + str(k))
            print("--- " + str(pi[k]))
            k = pi[k]
        k = k + 1
        pi[i] = k
        print("Pi = " + str(pi))
        print("---- fin boucle " + str(i))
    
    pi[0] = -1
    return pi

#print(preprocessing("ababababca",len("ababababca")))    


def matching(T,P,pi):
    k = -1
    for i in range (0,len(T)):
        print("*****debut de boucle ")
        print("k = " + str(k))
        print("pi[k]" + str(pi[k]))
        print("P[k+1]" + P[k+1])
        print("T[i]" + T[i])
        while k > -1 and P[k+1] != T[i]:
            print("dans la boucle k" + str(k))
            print("dans la boucle pi[" + str(k) + "]" + str(pi[k]))
            k = pi[k]
        k = k + 1
        if k == len(P)-1:
            print("match a " + str(i - k))
            k = pi[k]

#matching("ABC ABCDAB ABCDABCDABDE","ABCDABD",preprocessing("ABCDABD",len("ABCDABD")))

def put(P):
    P2 =[]
    P2.append(-1)
    for i in range(0, len(P)) :
        P2.append(P[i])
    return P2

def preprocessing2(P2,m):
    pi = []

    for i in range (0,m+1):
        pi.append(-1)
    
    #print(pi)
    
    k = -1
    for i in range (1,m+1):
        print("---- debut boucle " + str(i))
        print("k " + str(k))
        print("P[k+1]" + str(P2[k+1]))
        print("P[i]" + str(P2[i]))
        while(k >= 0 and P2[k+1] != P2[i]):
            #print("---" + str(k))
            #print("--- " + str(pi[k]))
            k = pi[k]
        k = k + 1
        pi[i] = k
        print("Pi = " + str(pi))
        print("---- fin boucle " + str(i))
    

    return pi
    
#print(preprocessing2("ABCDABD",len("ABCDABD")))


def matching2(T,P,pi):
    k = 0
    l = []
    for i in range (1,len(T)):
        print("*****debut de boucle " + str(i))
        print("k = " + str(k))
        print("pi[k]" + str(pi[k]))
        print("P[k+1]" + P[k+1])
        print("T[i]" + T[i])
        while k >= 0 and P[k+1] != T[i]:
            print("dans la boucle k" + str(k))
            print("dans la boucle pi[" + str(k) + "]" + str(pi[k]))
            i = i - 1
            k = pi[k]
        k = k + 1
        if k == len(P)-1:
            l.append(i-k)
            print("match a " + str(i - k))
            k = pi[k]
    return l

#print(preprocessing2(put("ABCDABD"),len("ABCDABD")))
print(matching2(put("ABC ABCDAB ABCDABCDABDE"),put("ABCDABD"),preprocessing2(put("ABCDABD"),len("ABCDABD"))))
#print(put("ABC ABCDAB ABCDABCDABDE"))


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
