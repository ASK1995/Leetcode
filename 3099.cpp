class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum_of_digits = 0;
        int num = x;
        while(num != 0) {
            sum_of_digits += num % 10;
            num /= 10;
        }
        if(x % sum_of_digits == 0) {
            return sum_of_digits;
        }
        return -1;
    }
};