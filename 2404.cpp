class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
        unordered_map<int, int> count;
        int max_count = -1, max_value = -1;

        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] % 2 == 0) {
                count[nums[i]]++;
                if(count[nums[i]] > max_count) {
                    max_count = count[nums[i]];
                    max_value = nums[i];
                } else if (count[nums[i]] == max_count) {
                    if(nums[i] < max_value) {
                        max_value = nums[i];
                    }
                }
            }
        }
        return max_value;
    }
};