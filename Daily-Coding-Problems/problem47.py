"""
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #47

Given a array of numbers representing the stock prices of a company
in chronological order, write a function that calculates the maximum
profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you
could buy the stock at 5 dollars and sell it at 10 dollars.

NOTE - 
min

"""


def single_pass_solution(stock_prices):
    profits = []
    local_min = stock_prices[0]
    local_max = stock_prices[0]

    for price in stock_prices:
        if price < local_min:
            profits.append(abs(local_max - local_min))
            local_min = local_max = price
        elif price > local_max:
            local_max = price

    profits.append(abs(local_max - local_min))

    return max(profits)


if __name__ == "__main__":
    print(single_pass_solution([9, 11, 8, 5, 7, 10]))
