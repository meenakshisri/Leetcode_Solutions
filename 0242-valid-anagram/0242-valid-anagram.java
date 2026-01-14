class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length()!=t.length())
        {
            return false;
        }

        int char_arr[] = new int[26];

        for(int i=0; i<s.length(); i++)
        {
            char_arr[s.charAt(i)-'a']++;
            char_arr[t.charAt(i)-'a']--;
        }

        for(int count : char_arr)
        {
            if(count != 0)
            {
                return false;
            }
        }
        return true;
    }
}