class Solution {
    public int[] getConcatenation(int[] nums) {
        
        int n = nums.length;
        int[] ans = new int[2*n];

        for(int i=0; i<2*n; i++)
        {
            if(i<n)
            {
                ans[i] = nums[i];
            }
            else
            {
                ans[i] = nums[i-n];
            }
        }
        return ans;
    }
}
/*
class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];
        System.arraycopy(nums, 0, ans, 0, n);
        System.arraycopy(nums, 0, ans, n, n);
        return ans;
    }
}
*/