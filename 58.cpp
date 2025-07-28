class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = 0, n = s.size();
        bool inside = false;

        for(i = s.size() - 1; i >= 0; i--) {
            if(s[i] == ' ') {
                if(inside) {
                    break;
                }
            } else {
                if(!inside) {
                    inside = true;
                    n = i;
                }
            }
        }

        return n - i;
    }
};