class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int ops = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] % 3 != 0) {
                ops += 1;
            }
        }
        return ops;
    }
};