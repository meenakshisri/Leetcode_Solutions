class Solution {
    public String mergeAlternately(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        StringBuilder res = new StringBuilder(m+n);

        int min = Math.min(m, n);

        for(int i = 0; i<min; i++)
        {
            res.append(word1.charAt(i));
            res.append(word2.charAt(i));
        }

        res.append(word1, min, m);
        res.append(word2, min, n);

        return res.toString();
    }
}