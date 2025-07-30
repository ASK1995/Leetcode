class Solution {
public:
    int mySqrt(int x) {
        int l = 0, r = x, m;
        unsigned long long val;

        while(l <= r) {
            m = l + (r - l)/2;
            val = (unsigned long long) m * m;
            if(val == x){
                return m;
            } else if (val > x) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return l - 1;
    }
};