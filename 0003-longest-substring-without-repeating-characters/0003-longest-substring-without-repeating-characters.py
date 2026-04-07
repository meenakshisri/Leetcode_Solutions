class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        char_Set = set()
        length = 0

        for r in range(len(s)):
            while s[r] in char_Set:
                char_Set.remove(s[l])
                l += 1

            char_Set.add(s[r])

            length = max(length, r-l+1)
        return length


        