#Perfect Numbers
class Solution:
    def isPerfectNumber(self, N: int) -> int:
        sum = 1
        i = 2
        while i * i <= N:
            if N % i == 0:
                if i == N // i:
                    sum += i
                else:
                    sum += i
                    sum += N // i
            i += 1
        
        if sum == N and N != 1:
            return 1
        else:
            return 0
