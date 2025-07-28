class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1, res = -1, m;
        vector<int> ans;
        while(l <= r) {
            m = l + (r - l)/2;
            if(nums[m] == target) {
                r = m - 1;
                res = m;
            } else if (nums[m] > target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        ans.push_back(res);
        l = 0;
        r = nums.size() - 1;
        res = -1;
        while(l <= r) {
            m = l + (r - l)/2;
            if(nums[m] == target) {
                l = m + 1;
                res = m;
            } else if (nums[m] > target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        ans.push_back(res);
        return ans;
    }
};