class Solution {
public:
    bool checkPerfectNumber(int num) {
        int i = 2, sum = 1;
        if(num <= 1) {return false;}

        while(i * i < num) {
            if(num % i == 0) {
                sum += i + num/i;
            }
            i++;
        }
        
        if(i * i == num) {
            sum += i;
        }

        return sum == num;
    }
};