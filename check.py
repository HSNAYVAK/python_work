S = "LOST"
L= [10,21,33,4]
D={}
for I in range (len(S)):
    if I%2==0:
        D[L.pop()] = S[I]
    else:
        D[L.pop()] = I+3
for K,V in D.items():
    print (K, V, sep="*")
