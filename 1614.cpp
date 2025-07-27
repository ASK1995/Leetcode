class Solution {
public:
    int maxDepth(string s) {
        int curr = 0, res = 0;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '(') {
                curr += 1;
            } else if(s[i] ==')') {
                curr -= 1;
            }
            res = fmax(curr, res);
        }

        return res;
    }
};