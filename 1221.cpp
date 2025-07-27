class Solution {
public:
    int balancedStringSplit(string s) {
        int res = 0, current = 0;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == 'L') {
                current -= 1;
            } else {
                current += 1;
            }
            if(current  == 0) {
                res++;
            }
        }
        return res;
    }
};