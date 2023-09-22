#Largest number possible
class Solution:
    def findLargest(self, N: int, S: int) -> str:
        ans = ""

        if S == 0 and N > 1:
            return "-1"

        for i in range(N):
            if S >= 9:
                ans += '9'
                S -= 9
            else:
                ans += str(S)
                S = 0

        if S > 0:
            return "-1"

        return ans
