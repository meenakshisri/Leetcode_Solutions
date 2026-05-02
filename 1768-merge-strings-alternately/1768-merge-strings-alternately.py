class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l1, l2 = 0, 0
        len1, len2 = len(word1), len(word2)
        res = ""

        while l1<len1 and l2<len2 :

            res = res + word1[l1] + word2[l2]
            l1 = l1+1
            l2 = l2+1
        
        if l1<len1:
            res = res + word1[l1:]
        if l2<len2:
            res = res +word2[l2:]
        
        return res

