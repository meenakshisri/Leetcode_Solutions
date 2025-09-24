class Solution {
    public int[] twoSum(int[] nums, int target) {

       HashMap<Integer,Integer> hMap = new HashMap<>();

       for(int i=0; i< nums.length; i++)
       {
            int complement = target - nums[i];

            if(hMap.containsKey(complement))
            {
                return new int[]{i,hMap.get(complement)};
            }
            hMap.put(nums[i], i);
       } 
       return new int[]{};
    }
}