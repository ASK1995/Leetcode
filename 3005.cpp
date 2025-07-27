class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> count;
        int max_count = 0, res = 0;

        for(int i = 0; i < nums.size(); i++) {
            count[nums[i]]++;
            max_count = fmax(max_count, count[nums[i]]);
        }
        for(auto it = count.begin(); it != count.end(); it++) {
            if(it->second == max_count) {
                res++;
            }
        }
        return res * max_count;
    }
};