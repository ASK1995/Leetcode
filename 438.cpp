class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char, int> count_s, count_p;
        int matches = 0, left = 0, count;
        vector<int> res;

        for(int i = 0; i < p.size(); i++) {
            count_p[p[i]]++;
        }
        count = count_p.size();

        for(int i = 0; i < s.size(); i++) {
            count_s[s[i]]++;
            if(count_s[s[i]] == count_p[s[i]]) {
                matches++;
            }
            if(i - left + 1 == p.size()) {
                if(matches == count) {
                    res.push_back(left);
                }
                if(count_s[s[left]] == count_p[s[left]]) {
                    matches--;
                }
                count_s[s[left]]--;
                if(count_s[s[left]] == 0) {
                    count_s.erase(s[left]);
                }
                left++;
            }
        }
        return res;
    }
};