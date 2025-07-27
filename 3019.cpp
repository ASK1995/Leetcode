class Solution {
public:
    int countKeyChanges(string s) {
        int res = 0;

        for(int i = 1; i < s.size(); i++) {
            if((s[i] == s[i - 1] + 32) || (s[i] == s[i - 1] - 32) || s[i] == s[i - 1]) {
                continue;
            }
            res++;
        }

        return res;
    }
};