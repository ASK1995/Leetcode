class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int curr = 0, res = 0;

        for(int i = 0; i < gain.size(); i++) {
            curr += gain[i];
            res = fmax(curr, res);
        }

        return res;
    }
};