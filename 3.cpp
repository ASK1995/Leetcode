class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> letters;
        int left = 0, longest = 0;

        for(int i = 0; i < s.size(); i++) {
            while(letters.find(s[i]) != letters.end()) {
                letters.erase(s[left]);
                left++;
            }
            letters.insert(s[i]);
            longest = max(longest, i - left + 1);
        }

        return longest;
    }
};