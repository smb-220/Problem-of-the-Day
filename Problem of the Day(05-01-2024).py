#Count possible ways to construct buildings
class Solution:
    def TotalWays(self, N):
        dpO=[0 for _ in range(0,N)]
        dpI=[0 for _ in range(0,N)]

        dpO[0]=1
        dpI[0]=1

        mod=10**9+7

        for i in range(1,N):
            dpO[i]=(dpO[i-1]+dpI[i-1])%mod

            dpI[i]=dpO[i-1]
        
        return ((dpO[N-1] + dpI[N-1])%mod*(dpO[N-1] + dpI[N-1])%mod)%mod
