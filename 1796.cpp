class Solution {
public:
    int secondHighest(string s) {
        int arr[10];
        bool first = false;

        for(int i = 0; i < s.size(); i++) {
            if(s[i] >= '0' && s[i] <= '9') {
                arr[s[i] - '0']++;
            }
        }
        for(int i = 9; i >= 0; i--) {
            if(arr[i] > 0) {
                if(!first) {
                    first = true;
                } else {
                    return i;
                }
            }
        }
        return -1;
    }
};