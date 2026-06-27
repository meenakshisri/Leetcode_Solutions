class Solution {
    public boolean isIsomorphic(String s, String t) {

        if(s.length() != t.length())
            return false;

        HashMap<Character, Character> s_to_t = new HashMap<>();
        HashMap<Character, Character> t_to_s = new HashMap<>();

        for(int i = 0; i<s.length(); i++)
        {
            char ch1 = s.charAt(i);
            char ch2 = t.charAt(i);

            if(s_to_t.containsKey(ch1))
            {
                if(s_to_t.get(ch1)!=ch2)
                {
                    return false;
                }
            }
            else{
                s_to_t.put(ch1, ch2);
            }

            if(t_to_s.containsKey(ch2))
            {
                if(t_to_s.get(ch2) != ch1)
                {
                    return false;
                }
            }
            else
            {
                t_to_s.put(ch2, ch1);
            }

        }

        return true;
       
    }
}