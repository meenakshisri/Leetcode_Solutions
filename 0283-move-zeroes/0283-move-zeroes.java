class Solution {
    public void moveZeroes(int[] nums) {

      int n = nums.length;
      int insertIndex = 0;
    
      for(int i = 0; i<n ; i++)
      {
        if(nums[i] != 0)
        {
            nums[insertIndex++] = nums[i];
        }
      }

      while(insertIndex<n)
      {
        nums[insertIndex++] = 0;
      }
    }
}