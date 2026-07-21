class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        l = 0
        maxSize = 0

        for r in range(len(s)):

            while s[r] in window:
                window.remove(s[l])
                l = l+1
            window.add(s[r])
            maxSize = max(maxSize, len(window))
        
        return maxSize


        