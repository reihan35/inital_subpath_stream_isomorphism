# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
  
    print("LPSSSS " + str(lps))
    i = 0 # index for txt[] 
    while i < N: 
        print("voici i " + str(i))
        print("voici j " + str(j))
        print(txt[i])
        print(pat[j])
        if pat[j] == txt[i]: 
            print "egale"
            i += 1
            j += 1
  
        if j == M: 
            print "Found pattern at index " + str(i-j) 
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                print ("not egale")
                j = lps[j-1] 
            else: 
                print ("not egale 2")
                i += 1
  
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
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
  
txt = "ABCDABABCDABCDABDE"
pat = "ABCDABD"
KMPSearch(pat, txt) 
  
# This code is contributed by Bhavya Jain 