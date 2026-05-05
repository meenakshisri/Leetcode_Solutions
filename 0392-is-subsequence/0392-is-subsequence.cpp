class Solution {
public:
    bool isSubsequence(string s, string t) {
        
        if(s.length()>t.length())
            return false;

        int l1 = 0, l2 = 0;

        while(l1<s.length() && l2<t.length())
        {
            if(s[l1] != t[l2])
            {
                l2++;
            }
            else
            {
                l1++;
                l2++;
            }           
        }
        if(l1>=s.length())
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};