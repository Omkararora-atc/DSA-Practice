class MyminHeap:
    def __init__(self):
        self.arr=[]
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-1)//2
    def Insert(self,x):
        arr=self.arr
        arr.append(x)
        i=len(arr)-1
        while i>0 and arr[self.parent(i)]>arr[i]:
            p=self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]
            i=p
    def min_heapify(self,i):
        arr=self.arr
        l=self.left(i)
        r=self.right(i)
        small=i
        n=len(self.arr)
        if l<n and arr[l]<arr[small]:
            small=l
        if r<n and arr[r]<arr[small]:
            small=r
        if small!=i:
            arr[i],arr[small]=arr[small],arr[i]
            self.min_heapify(small)
    def Extract_Min(self):
        arr=self.arr
        if len(arr)==0:
            return None
        if len(arr)==1:
            return arr[0]
        res=arr[0]
        arr[0]=arr[-1]
        arr.pop()
        self.min_heapify(0)
        return res
    def show(self):
        return self.arr
#### driver code
if __name__ == "__main__":
    heap = MyminHeap()
    heap.Insert(3)
    heap.Insert(1)
    heap.Insert(6)
    heap.Insert(5)
    heap.Insert(2)
    heap.Insert(4)
    print(heap.show())  # Output: [1, 2, 4, 5, 3, 6]
    print(heap.Extract_Min())  # Output: 1
    print(heap.show())  # Output: [2, 3, 4, 5, 6]
    heap.Insert(0)
    print(heap.show())  # Output: [0, 2, 4, 5, 3, 6]

