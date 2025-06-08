### find the second largest number in a list
def second(arr):
    if not arr:
        return None
    first , second = arr[0],None
    for i in arr:
        if i>first:
            second = first
            first = i
        elif  i != first:
            if second is None or i > second:
                second = i
    return second
## Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    second_largest = second(arr)
    print(f"Second largest value: {second_largest}")

    arr = [5, 4, 3, 2, 1]
    second_largest = second(arr)
    print(f"Second largest value: {second_largest}")

    arr = []
    second_largest = second(arr)
    print(f"Second largest value: {second_largest}")

    arr = [1]
    second_largest = second(arr)
    print(f"Second largest value: {second_largest}")