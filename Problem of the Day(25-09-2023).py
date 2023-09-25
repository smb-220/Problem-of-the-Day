import heapq
class findMaxSum:
    def __init__(self, A, B):
        self.A = sorted(A, reverse=True) 
        self.B = sorted(B, reverse=True)
        self.sums, self.visited = list(), set()
        self.__add_element(0, 0)
        
    def __call__(self):
        el_sum, indexes = heapq.heappop(self.sums)
        iA, iB = indexes
        self.__add_element(iA, iB + 1)
        self.__add_element(iA + 1, iB)
        return -el_sum
        
    def __add_element(self, iA, iB):
        indexes = iA, iB
        if iA < len(self.A) and iB < len(self.B) and indexes not in self.visited:
            heapq.heappush(self.sums, (-self.A[iA] - self.B[iB], indexes))
            self.visited.add(indexes)

class Solution:
    def maxCombinations(self, N, K, A, B):
        retriver = findMaxSum(A, B)
        return [retriver() for _ in range(K)]
