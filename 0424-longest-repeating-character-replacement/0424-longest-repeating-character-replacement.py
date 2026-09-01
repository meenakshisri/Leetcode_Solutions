class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Use of counter to keep track of character frequency
        window_len - maxFreq >k ??
        """
        count = {}
        l = 0
        length = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(count.values())

            while (r-l+1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            length = max(length, r-l+1)
        return length
        

            
