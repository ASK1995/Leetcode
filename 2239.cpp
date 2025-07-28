class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int res = nums[0];

        for(int i = 0; i < nums.size(); i++) {
            if(abs(res) > abs(nums[i])) {
                res = nums[i];
            } else if(abs(res) == abs(nums[i])) {
                res = fmax(res, nums[i]);
            }
        }
        return res;
    }
};