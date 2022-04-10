# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(startIdx,endIdx):
            while startIdx<endIdx:
                if s[startIdx]!=s[endIdx]:
                    return False
                startIdx+=1
                endIdx-=1
            return True    

        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return isPalindrome(i+1,j) or isPalindrome(i,j-1)
        return True
