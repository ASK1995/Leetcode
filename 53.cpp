class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int l = 0, sum = 0, max_sum = nums[0];
        for(int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            max_sum = max(max_sum, sum);
            while(sum < 0) {
                sum -= nums[l];
                l += 1;
            }
        }
        return max_sum;
    }
};