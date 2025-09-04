class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}

        if len(s) != len(t) :
            return False
        """
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t
        """
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1

        for char in t:
            if char not in count_s or count_s[char] == 0:
                return False
            count_s[char] -= 1

        return True


        