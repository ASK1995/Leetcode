class Solution {
public:
    vector<int> orArray(vector<int>& nums) {
        vector<int> res;
        for(int i = 0; i < nums.size() - 1; i++) {
            res.push_back(nums[i] | nums[i + 1]);
        }
        return res;
    }
};