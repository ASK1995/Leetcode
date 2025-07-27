class Solution {
public:
    int scoreOfString(string s) {
        int prev = s[0];
        int score = 0;
        for(int i = 1; i < s.size(); i++) {
            score += abs(int(s[i]) - int(s[i - 1]));
        }
        return score;
    }
};