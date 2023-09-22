#First and last occurrences of x
class Solution:
    def find(self, arr, n, x):
        ans = [-1, -1]

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                ans[0] = mid
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                ans[1] = mid
                left = mid + 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return ans
