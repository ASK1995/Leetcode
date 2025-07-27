class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int low = INT_MAX, max_profit = 0;
        for(int i = 0; i < prices.size(); i++) {
            if(prices[i] < low) {
                low = prices[i];
            }
            max_profit = fmax(max_profit, prices[i] - low);
        }
        return max_profit;
    }
};