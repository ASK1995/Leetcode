class FindSumPairs {
public:
    vector<int> v1, v2;
    unordered_map<int, int> counts;

    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        for(int i = 0; i < nums1.size(); i++){
            v1.push_back(nums1[i]);
        }
        for(int i = 0; i < nums2.size(); i++){
            v2.push_back(nums2[i]);
            counts[nums2[i]]++;
        }
    }
    
    void add(int index, int val) {
        counts[v2[index]]--;
        v2[index] += val;
        counts[v2[index]]++;
    }
    
    int count(int tot) {
        int res = 0;
        for(int i = 0; i < v1.size(); i++) {
            res += counts[tot - v1[i]];
        }

        return res;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */