class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
                
        unordered_set<int> s;

        for(int num : nums)
        {
            if(s.find(num) != s.end()) //O(1)
            {
                return true;
            }
            s.insert(num);  //O(1) for unordered set, and O(log n) for ordered set
        }
        return false;
        
    }
};