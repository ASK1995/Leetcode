class Solution {
public:
    int distinctAverages(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size() - 1;
        unordered_set<float> averages;

        for(int i = 0; i < nums.size(); i++) {
            cout << i << endl;
        }
        while(l < r) {
            averages.insert((float)(nums[l] + nums[r])/2);
            l++;
            r--;
        }
        return averages.size();
    }
};