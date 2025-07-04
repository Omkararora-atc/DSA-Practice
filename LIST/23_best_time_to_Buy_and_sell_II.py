### Popular leet code ques number 122
# ## write the code to find the maximum profit you can achieve from buying and selling a stock multiple times
def profit_max(arr):
    profit=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
    return profit
### driver code
if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    print(profit_max(arr))  # Output: 7
    arr = [1, 2, 3, 4, 5]
    print(profit_max(arr))  # Output: 4
    arr = [7, 6, 4, 3, 1]
    print(profit_max(arr))  # Output: 0