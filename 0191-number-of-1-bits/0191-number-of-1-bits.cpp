class Solution {
public:
    int hammingWeight(int n) {
        
        int count = 0;
        //Brian Kernighan's algorithm :  n = n & n-1 --> removes righmost set bit
        while(n>0)
        {
            n = n & n-1;
            count++;
        }

        return count;
    }
};