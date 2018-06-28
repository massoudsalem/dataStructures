# This MinHeap structure is written by Moh.Massoud in 28Jan18
class Heap:
    def __init__(self):
        self.heap = []
    def size(self):
        return len(self.heap) if len(self.heap) else print("The heap doesn't contain any elements.")
    def top(self):
        return self.heap[0] if len(self.heap) else print("The heap doesn't contain any elements.")
    def getLeftChild(self,node):
        child=2*node+1
        return child if child<len(self.heap) else -1
    def getRightChild(self,node):
        child=2*node+2
        return child if child<len(self.heap) else -1
    def getParent(self,node):
        return int((node-1)/2) if node!=0 else -1
    def reHeapUp(self,node):
        parent=self.getParent(node)
        if node == 0 or self.heap[parent]<self.heap[node]:
            return
        self.heap[parent],self.heap[node]=self.heap[node],self.heap[parent]
        self.reHeapUp(parent)
    def reHeapDown(self,node):
        minChild=self.getLeftChild(node)
        if minChild==-1:
            return
        rightChild=self.getRightChild(node)
        if self.heap[minChild]>self.heap[rightChild]:
            minChild=rightChild
        if self.heap[node]>self.heap[minChild]:
            self.heap[minChild], self.heap[node] = self.heap[node], self.heap[minChild]
            self.reHeapDown(minChild)
    def insertNode(self,node):
        self.heap.append(node)
        self.reHeapUp(self.size()-1)
    def removeTop(self):
        if self.size()!=0:
            self.heap[0]=self.heap[-1]
            self.heap.pop()
            self.reHeapDown(0)
    def printHeap(self):
        print(self.heap)

h=Heap()
h.insertNode(2)
h.insertNode(3)
h.insertNode(1)
h.insertNode(17)
h.insertNode(19)
h.insertNode(36)
h.insertNode(7)
h.insertNode(25)
h.insertNode(100)
h.printHeap()
h.removeTop()
h.printHeap()
h.removeTop()
h.printHeap()
h.removeTop()
h.printHeap()
h.removeTop()
h.printHeap()
h.removeTop()
h.printHeap()
h.removeTop()
h.printHeap()
h.removeTop()
h.printHeap()
h.removeTop()
h.printHeap()
h.removeTop()
h.printHeap()