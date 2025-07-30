class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> count;
        int start = 0, longest = 0, current_longest = 0;

        for(int i = 0; i < s.size(); i++) {
            count[s[i]]++;
            if(count[s[i]] > current_longest) {
                current_longest = count[s[i]];
            }
            while ((i - start + 1 - current_longest) > k) {
                count[s[start]]--;
                start++;
            }
            longest = fmax(longest, i - start + 1);
        }
        return longest;
    }
};