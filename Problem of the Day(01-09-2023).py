#Leftmost and rightmost nodes of binary tree
def printCorner(root):
    l=[1,root]
    lvl=[]
    while l:
        n=l.pop(0)
        i=0
        j=0
        tl=[]
        lv=[]
        while i<n:
            r=l.pop(0)
            lv.append(r)
            if r.left:
                j+=1
                tl.append(r.left)
            if r.right:
                j+=1
                tl.append(r.right)
            i+=1
        if j>0:
            l.append(j)
        if lv:
            lvl.append(lv)
            
                
        for e in tl:
            l.append(e)
            
    
    
    for e in lvl:
        if e:
            if len(e)>=2:
                print(e[0].data,e[-1].data,end=' ')
            else:
                print(e[0].data,end=' ')
