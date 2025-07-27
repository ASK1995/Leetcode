class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_jump = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(i > max_jump) {
                return false;
            }
            max_jump = fmax(max_jump, nums[i] + i);
        }
        return (max_jump >= nums.size() - 1);
    }
};