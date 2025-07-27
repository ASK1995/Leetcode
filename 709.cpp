class Solution {
public:
    string toLowerCase(string s) {
        string res;
        int curr = 0;

        for(int i = 0; i < s.size(); i++) {
            if(s[i] >= 65 and s[i] <= 90) {
                res += s[i] + 32;
            } else {
                res += s[i];
            }
        }

        return res;
    }
};