# coffre fort
def coffre_fort(m,d,c,u):
    rep = m%2==0 and m+c==15 and m+c==15 and d==c-m and m==u*d
    return rep

def decomposer(nb):
    u=nb%10
    d=int(nb/10)%10
    c=int(nb/100)%10
    m=int(nb/1000)%10
    return(m,c,d,u)
'''
programme principal qui devine le code
'''
for nb in range(1000,9999):
    (m,c,d,u)=decomposer(nb)
    if coffre_fort(m,c,d,u):
        print(nb)
