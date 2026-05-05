class Solution {
public:

    bool isAlphaNum(char c)
    {
        return ((c>='A' && c<='Z') || (c>='a' && c<='z') ||(c>='0' && c<='9'));
    }

    char toLowerCase(char c)
    {
        if(c>='A' && c<='Z')
            return c+32;
        else
            return c;
    }

    bool isPalindrome(string s) {
        
        int l = 0, r = s.length()-1;

        while(l<r)
        {
            while((l<r) && !isAlphaNum(s[l]))
            {
                l++;
            }
            while((l<r) && !isAlphaNum(s[r]))
            {
                r--;
            }
            if(toLowerCase(s[l]) != toLowerCase(s[r]))
            {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};