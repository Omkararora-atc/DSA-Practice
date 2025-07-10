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
    heap.Insert(0)
    print(heap.show())
