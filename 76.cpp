class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> count_s, count_t;
        int left = 0, smallest = s.size() + 1, start, matches = 0;
        int count;

        for(int i = 0; i < t.size(); i++) {
            count_t[t[i]]++;
        }

        count = count_t.size();
        for(int i = 0; i < s.size(); i++) {
            count_s[s[i]]++;
            if(count_s[s[i]] == count_t[s[i]]) {
                matches += 1;
            }
            while(matches == count) {
                if(smallest > i - left + 1) {
                    smallest = i - left + 1;
                    start = left;
                }
                if(count_s[s[left]] == count_t[s[left]]) {
                    matches--;
                }
                count_s[s[left]]--;
                if(count_s[s[left]] == 0) {
                    count_s.erase(s[left]);
                }
                left++;
            }
        }
        if(smallest == s.size() + 1) {
            return "";
        }
        return s.substr(start, smallest);
    }
};