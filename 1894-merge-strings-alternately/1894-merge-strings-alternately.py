class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        if not word1 and not word2:
            return None
            
        ptr1, ptr2 = 0, 0
        result = []

        while ptr1<len(word1) and ptr2<len(word2):
            result.append(word1[ptr1])
            result.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1
        result.append(word1[ptr1:])
        result.append(word2[ptr2:])
        return "".join(result)

     