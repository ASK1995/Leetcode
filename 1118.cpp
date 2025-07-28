class Solution {
public:
    int numberOfDays(int year, int month) {
        int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if(month != 2) {
            return days[month - 1];
        }
        if(month == 2 && year % 4 == 0) {
            if(year % 100 == 0) {
                if(year % 400 != 0) {
                    return 28;
                }
                return 29;
            }
            return 29;
        }
        return 28;
    }
};