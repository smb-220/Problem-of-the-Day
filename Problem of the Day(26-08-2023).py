#Longest K unique characters substring
class Solution:
    def longestKSubstr(self, s, k):
        m = {}
        for x in s:
            m[x] = 0

        uniq = 0
        i = 0
        j = 0
        res = 0
        n = len(s)
        
        while j < n:
            while j < n:
                if m[s[j]] == 0:
                    uniq += 1
                m[s[j]] += 1
                if uniq > k:
                    break
                j += 1
            if uniq >= k:
                res = max(res, j-i)
            if j == n:
                break
            while i < n:
                if m[s[i]] == 1:
                    uniq -= 1
                
                m[s[i]] -= 1
                if uniq == k:
                    break
                i += 1
            i += 1
            j += 1
        if res == 0:
            return -1
        return res
