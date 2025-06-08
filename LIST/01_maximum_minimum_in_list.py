### find the maximum and minimum in a list
def find_max_min(lst):
    if not lst:
        return None, None  # Handle empty list case

    max_val=lst[0]
    min_val=lst[0]
    for i in lst:
        if i> max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return max_val, min_val
## Driver code
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    max_val, min_val = find_max_min(lst)
    print(f"Maximum value: {max_val}, Minimum value: {min_val}")

    lst = [5, 4, 3, 2, 1]
    max_val, min_val = find_max_min(lst)
    print(f"Maximum value: {max_val}, Minimum value: {min_val}")

    lst = []
    max_val, min_val = find_max_min(lst)
    print(f"Maximum value: {max_val}, Minimum value: {min_val}")