class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> res;
        int current = 0;

        for(int i = 0; i < nums.size(); i++) {
            current += nums[i];
            res.push_back(current);
        }
        return res;
    }
};