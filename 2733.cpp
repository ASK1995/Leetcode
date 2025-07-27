class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        int max, min;
        max = *max_element(nums.begin(), nums.end());
        min = *min_element(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] != max && nums[i] != min) {
                return nums[i];
            }
        }
        return -1;
    }
};