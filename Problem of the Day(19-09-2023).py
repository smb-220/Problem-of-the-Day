#Find first set bit
class Solution:
    def getFirstSetBit(self,n):
        if(n==0):
            return 0
        return math.ceil(math.log2(n&-n)+1)
