class Solution {
public:
    int minPartitions(string n) {
        int max_digit = 1;
        for(int i = 0; i < n.size(); i++) {
            max_digit = fmax(n[i] - '0', max_digit);
        }
        return max_digit;
    }
};