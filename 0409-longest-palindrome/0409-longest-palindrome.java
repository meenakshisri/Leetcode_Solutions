class Solution {
    public int longestPalindrome(String s) {
        
        int length = 0;
        boolean foundOdd = false;

        HashMap<Character, Integer> map = new HashMap<>();

        for(char ch:s.toCharArray())
        {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for(int val : map.values())
        {           
            if(val%2 == 0)
            {
                length += val;
            }
            else
            {
                length += val-1;
                foundOdd = true;
            }
        }

        if(foundOdd)
            return length+1;
        else
            return length;
    }
}