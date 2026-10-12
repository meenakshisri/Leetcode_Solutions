class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> window = new HashSet<>();
        int l = 0;
        int maxLen = 0;

        for(int r = 0; r<s.length(); r++)
        {
            char c = s.charAt(r);
            while(window.contains(c))
            {
                window.remove(s.charAt(l));
                l++;
            }

            window.add(c);
            maxLen = Math.max(maxLen, window.size());
        }
        return maxLen;
    }
}
