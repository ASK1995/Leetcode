class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> count;
        unordered_set<int> counts;

        for(int i = 0; i < arr.size(); i++) {
            count[arr[i]]++;
        }
        for(auto it = count.begin(); it != count.end(); it++) {
            if(counts.find(it->second) == counts.end()) {
                counts.insert(it->second);
            } else {
                return false;
            }
        }
        return true;
    }
};