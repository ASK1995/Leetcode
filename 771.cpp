class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_set<char> check;
        int res = 0;
        for(int i = 0; i < jewels.size(); i++) {
            check.insert(jewels[i]);
        }
        for(int j = 0; j < stones.size(); j++) {
            if(check.find(stones[j]) != check.end()) {
                res += 1;
            }
        }
        return res;
    }
};