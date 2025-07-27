class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int res = 0, digits, num;

        for(int i = 0; i < nums.size(); i++) {
            num = nums[i];
            digits = 0;
            while(num != 0) {
                num /= 10;
                digits++;
            }
            if(digits % 2 == 0) {
                res++;
            }
        }
        return res;
    }
};