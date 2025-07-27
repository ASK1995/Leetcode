class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int res = 0, n;
        for(int i = 0; i < operations.size(); i++) {
            if(operations[i][0] == '+' || operations[i][2] == '+') {
                res += 1;
            } else {
                res -= 1;
            }
        }
        return res;
    }
};