#ex1
def dist_Hamming(c1,c2):
    dist=0
    p=None
    if len(c1)<len(c2):
         p=c1
         dist=len(c2)-len(c1)
    else:
         p=c2
         dist=len(c1)-len(c2)
    for i in range (len(p)):
        if c1[i] != c2[i] :
            dist+=1
    return dist



#ex2
def dist_inf(lexique,m,d):
    mots_inf=""
    for mot in lexique:
        if dist_Hamming(mot,m)<=d:
             mots_inf+=mot+" "
            
    return mots_inf



#ex3
def dist_min(lexique,m):
    min=lexique[0]
    for i in range(len(lexique)-1):
        if dist_Hamming(min,m)>dist_Hamming(lexique[i+1],m):
            min=lexique[i+1]
    return min

print (dist_min(["amer","ramer","arbre","arabe","atistique","artiste","art","navigation"],"navigati"))