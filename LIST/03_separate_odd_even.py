### Separate odd and even numbers from a list
def separate(arr):
    if not arr:
        return [],[]
    odd = []
    even = []
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even
## Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    odd, even = separate(arr)
    print(f"Odd numbers: {odd}, Even numbers: {even}")

    arr = [5, 4, 3, 2, 1]
    odd, even = separate(arr)
    print(f"Odd numbers: {odd}, Even numbers: {even}")

    arr = []
    odd, even = separate(arr)
    print(f"Odd numbers: {odd}, Even numbers: {even}")

    arr = [1]
    odd, even = separate(arr)
    print(f"Odd numbers: {odd}, Even numbers: {even}")
    