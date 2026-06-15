class Solution {
public:
    bool isPalindrome(string s) {

       int l = 0;
       int r = s.size();

       while(l<r)
       {
            while(l<r && !isalnum(s[l])) //isalnum is built-in function
                l++;
            while(l<r && !isalnum(s[r]))
                r--;
            if(tolower(s[l]) != tolower(s[r])) //tolower is built-in function
            {
                return false;
            } 
            l++;
            r--;
       }
       return true; 
    }
};