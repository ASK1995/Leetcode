class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> unique_nums;
        for(int i = 0; i < nums.size(); i++) {
            if(unique_nums.find(nums[i]) != unique_nums.end()) {
                return true;
            }
            unique_nums.insert(nums[i]);
        }
        return false;
    }
};