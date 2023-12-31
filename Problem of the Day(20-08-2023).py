#Number of occurrence
import bisect
class Solution:
  def count(self, arr, n, x):
    low = bisect.bisect_left(arr, x)

      if low == n or arr[low] != x:
      return 0

      high = bisect.bisect_right(arr, x, low)
      return high - low
