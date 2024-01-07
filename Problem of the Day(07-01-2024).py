#Split Array Largest Sum
class Solution:
    def check(self, mid, array, n, K):
        count = 0
        sum = 0
        for i in range(n):
            if (array[i] > mid):
                return False
            sum += array[i]
     
            if (sum > mid):
                count += 1
                sum = array[i]
        count += 1
     
        if (count <= K):
            return True
        return False
        
    def splitArray(self, arr, N, K):
        
        start = max(arr)
        end = sum(arr)
     
        answer = 0
        while (start <= end):
            mid = (start + end) // 2
     
            if (self.check(mid, arr, N, K)):
                answer = mid
                end = mid - 1
            else:
                start = mid + 1
     
        return answer
