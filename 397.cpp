class Solution {
public:
    int integerReplacement(int n) {
        int res = 0;
        while(n != 1) {
            if(n % 2 == 0) {
                n /= 2;
            } else if (n != 3 and (n & 3 == 3)) {
                n++;
            } else {
                n--;
            }
            res++;
        }
        return res;
    }
};