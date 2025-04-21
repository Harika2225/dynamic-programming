class Solution:
    def stockBuySell(self, arr, n):
        if n == 0:
            return 0

        min_price = arr[0]
        max_profit = 0

        for i in range(1, n):
            if arr[i] < min_price:
                min_price = arr[i]
            else:
                profit = arr[i] - min_price
                max_profit = max(max_profit, profit)

        return max_profit