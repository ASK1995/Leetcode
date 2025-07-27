class Solution {
public:
    int differenceOfSums(int n, int m) {
        int total_sum = (n * (n + 1))/2;
        int num1, num2 = 0;
        for(int i = 1; i <= n; i++) {
            if(i % m  == 0) {
                num2 += i;
            }
        }
        num1 = total_sum - num2;
        return num1 - num2;
    }
};