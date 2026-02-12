class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0]

        for i in range(len(strs[0])):

            for str in strs:

                if (i ==len(str)) or (prefix[i] != str[i]):
                    return prefix[:i]

        return prefix
