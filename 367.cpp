class Solution {
public:
    bool isPerfectSquare(int num) {
        int l = 1, r = num, m;
        unsigned long long prod;

        while(l <= r) {
            m = l + (r - l)/2;
            prod = (unsigned long long) m * m;
            if(prod == num) {
                return true;
            } else if (prod > num) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return false;
    }
};