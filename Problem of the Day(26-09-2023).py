class Solution:
    def fourSum(self, a, k):
        n=len(a)
        ans=[]
        if(n < 4):
            return ans
        a.sort()
        for i in range(0, n-3):
            if (a[i] > 0 and a[i] > k):
                break
            if (i > 0 and a[i] == a[i - 1]):
                continue
            
            for j in range(i+1, n-2):
                if (j > i + 1 and a[j] == a[j - 1]):
                    continue
                left = j + 1
                right = n - 1
                while (left < right):
                    old_l = left;
                    old_r = right;
                    sum = a[i] + a[j] + a[left] + a[right]
                    if (sum == k):
                        ans.append([a[i], a[j], a[left], a[right]])
                        while (left < right and a[left] == a[old_l]):
                            left+=1
                        while (left < right and a[right] == a[old_r]):
                            right-=1
                    elif (sum > k):
                        right-=1
                    else:
                        left+=1
                    
        return ans;
