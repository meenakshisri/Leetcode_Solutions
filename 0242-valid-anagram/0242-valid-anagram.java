class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length())
        {
            return false;
        }

        int[] charArr = new int[26];

        for(int i = 0; i<s.length(); i++)
        {
            char ch = s.charAt(i);
            charArr[ch-'a']++;
        }

        for(int j = 0; j<t.length(); j++)
        {
            char ch = t.charAt(j);
            charArr[ch-'a']--;
        }

        for(int ch: charArr)
        {
            if(ch!=0)
                return false;
        }
        return true;
    }
}