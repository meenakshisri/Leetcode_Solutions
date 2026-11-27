class Solution {
public:
    int hammingWeight(int n) {

        string res ="";
        int count = 0;
        while(n!=1)
        {
            int rem = n%2;
            if(rem == 1)
            {
                count++;
            }
            res = to_string(rem) + res;
            n = n/2;
        }
        return count+1;
    }
};