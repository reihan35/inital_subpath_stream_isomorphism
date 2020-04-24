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

print(preprocessing("ababababca",len("ababababca")))    