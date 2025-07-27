class Solution {
public:
    int totalReplacements(vector<int>& ranks) {
        int current_min = ranks[0], res = 0;
        for(int i = 0; i < ranks.size(); i++) {
            if(ranks[i] < current_min) {
                res += 1;
                current_min = fmin(current_min, ranks[i]);
            }
        }
        return res;
    }
};