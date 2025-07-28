class Solution {
public:
    int countElements(vector<int>& nums) {
        int max_num = *max_element(nums.begin(), nums.end());
        int min_num = *min_element(nums.begin(), nums.end());
        int res = 0;

        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] > min_num && nums[i] < max_num) {
                res++;
            }
        }
        return res;
    }
};