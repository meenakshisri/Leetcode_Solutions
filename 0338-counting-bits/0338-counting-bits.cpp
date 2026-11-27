class Solution {
public:
    vector<int> countBits(int n) {

        vector<int> ans(n+1);
        
        for(int i = 0; i<n+1; i++)
        {
            int count = 0;
            int num = i;

            while(num>0)
            {
                num = num & (num-1);
                count++;
            }
            ans[i] = count;
        }

        return ans;
    }
};