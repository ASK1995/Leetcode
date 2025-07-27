class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        unordered_map<int, int> count;
        int res = 0;

        for(int i = 0; i < nums.size(); i++) {
            count[nums[i]]++;
        }

        for(auto it = count.begin(); it != count.end(); it++) {
            if(it->second == 1) {
                res += it->first;
            }
        }
        return res;
    }
};