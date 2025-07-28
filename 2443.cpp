class Solution {
public:
    bool sumOfNumberAndReverse(int num) {
        int i = 0, rev_num = 0, temp;
        while(i <= num) {
            temp = i;
            rev_num = 0;
            while(temp != 0) {
                rev_num = rev_num * 10 + temp % 10;
                temp /= 10;
            }
            if(rev_num + i == num) {
                return true;
            }
            i++;
        }
        return false;
    }
};