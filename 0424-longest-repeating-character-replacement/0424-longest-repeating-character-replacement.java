class Solution {
    public int characterReplacement(String s, int k) {

       int[] count = new int[26];
       int maxFreq = 0;
       int l = 0;
       int maxLen = 0;

       for(int i = 0; i<s.length(); i++)
       {
        count[s.charAt(i)-'A']++;

        maxFreq = Math.max(maxFreq, count[s.charAt(i)-'A']);

        while((i-l+1)-maxFreq>k)
        {
            count[s.charAt(l)-'A']--;
            l++;
        }
        maxLen = Math.max(maxLen, i-l+1);

       } 
       return maxLen;
    }
}
