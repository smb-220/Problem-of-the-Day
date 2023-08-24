#Palindrome String
class Solution:
    def isPalindrome(self, S: str) -> int:
        for i in range(len(S) // 2):
            if S[i] != S[len(S) - i - 1]:
                return 0
        return 1