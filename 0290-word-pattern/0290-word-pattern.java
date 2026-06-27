class Solution {
    public boolean wordPattern(String pattern, String s) {
        
        String words[] = s.split(" ");

        if(words.length != pattern.length())
        {
            return false;
        }

        HashMap<Character, String> mp1 = new HashMap<>();
        HashMap<String, Character> mp2 = new HashMap<>();

        for(int i=0; i<pattern.length(); i++)
        {
            char ch1 = pattern.charAt(i);
            String word = words[i];

            if(mp1.containsKey(ch1))
            {
                if(!mp1.get(ch1).equals(word))
                {
                    return false;
                }
            }
            else
            {
                mp1.put(ch1, word);
            }

            if(mp2.containsKey(word))
            {
                if(!mp2.get(word).equals(ch1))
                {
                    return false;
                }
            }
            else
            {
                mp2.put(word, ch1);
            }
        }

        return true;
    }
}