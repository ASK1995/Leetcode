class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int l = 0, r = letters.size() - 1, m, res;

        res = letters[0];
        while(l <= r) {
            m = l + (r - l)/2;
            if(letters[m] > target) {
                res = letters[m];
                r = m - 1;
            } else{
                l = m + 1;
            }
        }
        return res;
    }
};