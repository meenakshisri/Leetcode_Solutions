class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        l = 0
        length = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            length = max(length, len(window)) # can use r-l+1 also in place of len (window)
        
        return length
        