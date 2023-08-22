#Leaders in an array
class Solution:
    def leaders(self, A, N):
        ans=[]
        maxx=A[N-1]
    
        for i in range(N-1,-1,-1):
            if A[i]>=maxx:
                maxx=A[i]
                ans.append(maxx)
        ans.reverse()
        return ans
