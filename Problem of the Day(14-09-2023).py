class Solution:
    def __init__(self):
        self.mod = int(1e9 + 7)  
        self.dp = []  
        self.N = 0  

    def fun(self, pos, sum, arr):
        if pos >= self.N:
            return int(sum == 0)  

        ans = self.dp[pos][sum]
        if ans != -1:
            return ans  

        ans = 0  

        ans += self.fun(pos + 1, sum, arr)  
        ans %= self.mod  
        if arr[pos] <= sum:
            ans += self.fun(pos + 1, sum - arr[pos], arr)
            ans %= self.mod 

        self.dp[pos][sum] = ans  
        return ans  

    def perfectSum(self, arr, n, sum):
        self.dp = [[-1] * (sum + 2) for _ in range(n + 1)]  
        self.N = n 
        return self.fun(0, sum, arr)  
