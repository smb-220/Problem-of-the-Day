#Leaf under budget
class Solution:
    def budg(self,root,d,lv):
        if not root:
            return
        if not root.left and not root.right:
            if lv in d:
                d[lv]+=1
            else:
                d[lv]=1
            return
        self.budg(root.left,d,lv+1)
        self.budg(root.right,d,lv+1)
    def getCount(self,root,n):
        d=dict()
        self.budg(root,d,1)
        
        c=0
        s=0
        for k in sorted(d):
            if s+(d[k]*k)>=n:
                break
            s+=(d[k]*k)
            c+=d[k]
        else:
            return c
        lb=n-s
        ln=lb//k
        if d[k]>=ln:
            c+=ln
            return c
        else:
            return c+d[k]
