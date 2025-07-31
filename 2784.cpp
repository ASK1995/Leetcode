class Solution {
public:
    bool isGood(vector<int>& nums) {
        unordered_set<int>count;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] >= nums.size()) {
                return false;
            }
            if(count.find(nums[i]) != count.end()) {
                if(nums[i] != nums.size() - 1) {
                    return false;
                }
            }
            count.insert(nums[i]);
        }
        return nums.size() - 1 == count.size();
    }
};