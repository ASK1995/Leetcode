class Solution {
public:
    int arrangeCoins(int n) {
        int l = 0, r = n, m, res = 0;
        unsigned long long prod;

        while(l <= r) {
            m = l + (r - l)/2;
            prod = (unsigned long long) m * (m + 1)/2;
            if(prod <= n) {
                res = m;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return res;
    }
};