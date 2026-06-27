class Solution {
    public int majorityElement(int[] nums) {
        //BOYER_MOORE ALGORITHM

        int candidate = nums[0];
        int count = 0;

        for(int i = 0; i<nums.length; i++)
        {
            if(count == 0)
            {
                candidate = nums[i];
                count = 1;
            }
            else
            {
                if(candidate == nums[i])
                {
                    count += 1;
                }
                else
                {
                    count += -1;
                }
            }
        }
        return candidate;
    }
}