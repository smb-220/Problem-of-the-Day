class Solution:
    def atMostK (self,s, k):
        if k < 0:
            return 0
            
        i = 0
        j = 0
        cnt = 0
        res = 0
        m = [0 for i in range (26)]
        
        while j < len (s):
            m[ord (s[j]) - ord ('a')] += 1
            if m[ord (s[j]) - ord ('a')] == 1:
                cnt += 1
            
            while cnt > k:
                m[ord (s[i]) - ord ('a')] -= 1
                if m[ord (s[i]) - ord ('a')] == 0:
                    cnt -= 1
                i += 1
            
            res += j - i + 1
            j += 1
        return res
    
    def substrCount (self,s, k):
        return self.atMostK (s, k) - self.atMostK (s, k-1)
