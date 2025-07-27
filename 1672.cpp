class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int res, total;
        for(int i = 0; i < accounts.size(); i++) {
            total = 0;
            for(int j = 0; j < accounts[i].size(); j++) {
                total += accounts[i][j];
            }
            res = fmax(res, total);
        }
        return res;
    }
};