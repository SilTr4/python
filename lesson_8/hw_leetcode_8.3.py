# 26. Remove Duplicates from Sorted Array

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[i::-1] + word[i+1:]
        return word