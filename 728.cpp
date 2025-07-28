class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        int num, digit;
        bool div;

        for(int i = left; i <= right; i++) {
            num = i;
            div = true;
            while(num != 0) {
                digit = num % 10;
                num /= 10;
                if(digit == 0) {
                    div = false;
                    break;
                }
                if(i % digit != 0) {
                    div = false;
                    break;
                }
            }
            if(div) {
                res.push_back(i);
            }
        }
        return res;
    }
};