#Print first n Fibonacci Numbers
class Solution:
    def printFibb(self,n):
        res = []
        a=b=1
        if n>=1:
            res.append (1)
        if n>=2:
            res.append (1)
        for i in range(2,n):
            res.append (a+b)
            c=a+b
            a=b
            b=c
        return res
