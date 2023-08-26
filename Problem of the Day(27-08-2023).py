#Reverse a String
class Solution:
    def reverseWord(self, str: str) -> str:
        rev = ""
        for i in range(len(str)-1, -1, -1):
            rev += str[i]
        return rev
