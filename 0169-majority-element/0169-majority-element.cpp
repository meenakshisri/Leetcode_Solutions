class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        //Boyer-Moore Voting Algo
        //Three Conditions:
        //1. Count is 0, reset
        //2. Current equal to candidate
        //3. else: currenmt not equal to candidate

        int candidate = nums[0];
        int count = 1;

        for(int i =1; i<nums.size(); i++)
        {
            if(count == 0)
            {
                candidate = nums[i];
                count = 1;
            }
            else if(nums[i] == candidate)
            {
                count++;
            }
            else
            {
                count--;
            }
        }
        return candidate;
    }
};