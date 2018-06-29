# This binarySearchTree structure is written by Moh.Massoud in 29Jan18
class node:
    def __init__(self,value=None,freq=1):
        self.value=value
        self.freq=freq
        self.rChild=None
        self.lChild=None
        self.perent=None
class binarySearchTree:
    def __init__(self,list=[]):
        self.root=None
        self.str=""
        for i in list:
            self.insert(i)
    def __str__(self):
        Str=self._printTree()
        return Str if Str!="[]" else "This tree is empty."

    def insert(self, value):
        if self.root==node(value):
            self.root.freq+=1
        elif self.root==None:
            self.root=node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, currNode):
        if value>currNode.value:
            if currNode.rChild==None:
                currNode.rChild=node(value)
                currNode.rChild.perent=currNode
            else:
                self._insert(value,currNode.rChild)
        elif value<currNode.value:
            if currNode.lChild==None:
                currNode.lChild=node(value)
                currNode.lChild.perent=currNode
            else:
                self._insert(value,currNode.lChild)
        else:
            currNode.freq+=1
    def height(self): # DFS traverse for finding height.
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,node,currHeight):
        if node==None:
            return currHeight
        lHeight=self._height(node.lChild,currHeight+1)
        rHeight=self._height(node.rChild,currHeight+1)
        return max(lHeight,rHeight)

    def _printTree(self):
        self.str = ""
        if self.root!=None:
            self._genStr(self.root)
        self.str=self.str[:-2]
        return "["+self.str+"]"

    def _genStr(self, currNode):
        if currNode==None:
            return
        else:
            self._genStr(currNode.lChild)
            for i in range(currNode.freq):
                self.str+= "{}, ".format(currNode.value)
            self._genStr(currNode.rChild)

    def findNode(self,value):
        if self.root!=None:
            return self._findNode(value,self.root)
        else:
            return None

    def _findNode(self,value,currNode):
        if currNode.value==value:
            return currNode
        elif currNode.value>value and currNode.lChild!=None:
            return self._findNode(value,currNode.lChild)
        elif currNode.value<value and currNode.rChild!=None:
            return self._findNode(value,currNode.rChild)
        return None

    def search(self,value):
        return True if self.findNode(value) else False

    def delete(self,value):
        return self._delete(self.findNode(value))

    def _delete(self,node):
        if node==None or self.findNode(node.value)==None:
            print("Node is not found!")
            return
        def findMinNode(node):
            currNode=node
            if currNode.lChild==None:
                return currNode
            else:
                return findMinNode(currNode.lChild)
        def childrenNum(node):
            num=0;
            if node.rChild!=None:
                num+=1
            if node.lChild!=None:
                num+=1
            return num
        if node.freq>1:
            node.freq-=1
        else:
            nodeChildern=childrenNum(node)
            nodePerent=node.perent
            if nodeChildern==0:
                if nodePerent!=None:
                    if nodePerent.lChild==node:
                        nodePerent.lChild=None
                    else:
                        nodePerent.rChild=None
                else:
                    self.root=None
            if nodeChildern==1:
                if node.lChild!=None:
                    child=node.lChild
                else:
                    child=node.rChild
                if nodePerent!=None:
                    if nodePerent.lChild==node:
                        nodePerent.lChild=child
                    else:
                        nodePerent.rChild=child
                else:
                    self.root=child
                child.perent=nodePerent
            if nodeChildern==2:
                minChild=findMinNode(node.rChild)
                node.value=minChild.value
                self._delete(minChild)


y=[4,4,3,5,2,1]
print(y,"is a list")
y=binarySearchTree(y)
print(y ,"is binarySearchTree")
print(y.height())
y.delete(4)
print(y)
y.delete(4)
print(y)
y.delete(4)
print(y)
y.delete(5)
print(y)
y.insert(4)
print(y)
print("{} {}".format("Searching for 1:\n","Found!"if y.search(1) else "Not found!"))
y.delete(1)
print(y)
print("{} {}".format("Searching for 1:\n","Found!"if y.search(1) else "Not found!"))
y.insert(0)
print(y)
print("{} {}".format("Searching for 0:\n","Found!"if y.search(0) else "Not found!"))
print(y.height())
y.delete(0)
y.delete(2)
print(y.height())
y.delete(3)
print(y.height())
y.delete(4)
print(y.height())
print(y)
