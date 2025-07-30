class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> count1;
        vector<int> res;

        for(int i = 0; i < nums1.size(); i++) {
            count1[nums1[i]]++;
        }
        for(int i = 0; i < nums2.size(); i++) {
            if(count1[nums2[i]] > 0) {
                count1[nums2[i]]--;
                res.push_back(nums2[i]);
            }
        }

        return res;
    }
};