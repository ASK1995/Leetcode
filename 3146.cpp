class Solution {
public:
    int findPermutationDifference(string s, string t) {
        unordered_map<char, int> count;
        int res = 0;

        for(int i = 0; i < s.size(); i++) {
            count[s[i]] += i;
        }
        for(int i = 0; i < t.size(); i++) {
            count[t[i]] -= i;
            res += abs(count[t[i]]);
        }

        return res;        
    }
};