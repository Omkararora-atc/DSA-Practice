def stock(arr):
    max_profit=0
    min_profit=float('inf')
    for price in arr:
        if price<min_profit:
            min_profit=price
        profit=price-min_profit
        if profit>max_profit:
            max_profit=profit
    return max_profit
# Example usage
if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    result = stock(arr)
    print(f"Maximum profit from stock prices {arr}: {result}")  # Output: Maximum profit from stock prices [7, 1, 5, 3, 6, 4]: 5

    arr = [7, 6, 4, 3, 1]
    result = stock(arr)
    print(f"Maximum profit from stock prices {arr}: {result}")  # Output: Maximum profit from stock prices [7, 6, 4, 3, 1]: 0

    arr = [1]
    result = stock(arr)
    print(f"Maximum profit from stock prices {arr}: {result}")  # Output: Maximum profit from stock prices [1]: 0
