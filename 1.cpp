class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> index_map;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            if(index_map.find(target - nums[i]) != index_map.end()) {
                res.push_back(index_map[target - nums[i]]);
                res.push_back(i);
            }
            index_map[nums[i]] = i;
        }
        return res;
    }
};