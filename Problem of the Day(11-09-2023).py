class Solution:
    def check(self, n,c):
        if(c<=n):
            if n%c==0:
                c=2
                return False;
            n = n-n//c
            c+=1
            return self.check(n,c)
        
        else:
            return True
    def isLucky(self, n): 
        return self.check(n,2)
