class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> count;
        if(s.size() != t.size()) {
            return false;
        }
        for(int i = 0; i < s.size(); i++) {
            count[s[i]] += 1;
        }
        for(int i = 0; i < t.size(); i++) {
            count[t[i]] -= 1;
            if(count[t[i]] < 0) {
                return false;
            }
        }
        return true;
    }
};