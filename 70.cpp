class Solution {
public:
    int climbStairs(int n) {
        if(n < 3) {
            return n;
        }
        int temp, prev = 2, curr = 3;

        for(int i = 4; i <= n; i++) {
            temp = prev;
            prev = curr;
            curr = curr + temp;
        }
        return curr;
    }
};