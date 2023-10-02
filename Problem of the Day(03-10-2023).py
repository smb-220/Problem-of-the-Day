class Solution: 
    def colName (self, n):
        res = ""
        while n > 0:
            n -= 1
            temp = n % 26
            res += chr (ord('A') + temp)
            n //= 26
        res = res[::-1]
        return res
