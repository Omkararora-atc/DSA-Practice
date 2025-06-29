def perfect(num):
    if num < 0:
        return False
    if num == 0 or num == 1:
        return True
    left, right = 2, num // 2
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False
# Example usage
if __name__ == "__main__":
    test_numbers = [16, 14, 25, 0, 1, -4]
    for num in test_numbers:
        result = perfect(num)
        print(f"Is {num} a perfect square? {result}")
