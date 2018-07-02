# This binarySearchTree structure is written by Moh.Massoud in 01July18
class node:
    def __init__(self, value=None, freq=1):
        self.value = value
        self.freq = freq
        self.rChild = None
        self.lChild = None
        self.perent = None
        self.height = 1


class AVLTree:
    def __init__(self, list=[]):
        self.root = None
        self.str = ""
        for i in list:
            self.insert(i)

    def __str__(self):
        Str = self._printTree()
        return Str if Str != "[]" else "This Tree is empty."

    def insert(self, value):
        if self.root == node(value):
            self.root.freq += 1
        elif self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, currNode):
        if value > currNode.value:
            if currNode.rChild == None:
                currNode.rChild = node(value)
                currNode.rChild.perent = currNode
                self._insBalancing(currNode.rChild)
            else:
                self._insert(value, currNode.rChild)
        elif value < currNode.value:
            if currNode.lChild == None:
                currNode.lChild = node(value)
                currNode.lChild.perent = currNode
                self._insBalancing(currNode.lChild)
            else:
                self._insert(value, currNode.lChild)
        else:
            currNode.freq += 1

    def height(self):  # DFS traverse for finding height.
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, node, currHeight):
        if node == None:
            return currHeight
        lHeight = self._height(node.lChild, currHeight + 1)
        rHeight = self._height(node.rChild, currHeight + 1)
        return max(lHeight, rHeight)

    def _printTree(self):
        self.str = ""
        if self.root != None:
            self._genStr(self.root)
        self.str = self.str[:-2]
        return "[" + self.str + "]"

    def _genStr(self, currNode):
        if currNode == None:
            return
        else:
            self._genStr(currNode.lChild)
            for i in range(currNode.freq):
                self.str += "{}, ".format(currNode.value)
            self._genStr(currNode.rChild)

    def findNode(self, value):
        if self.root != None:
            return self._findNode(value, self.root)
        else:
            return None

    def _findNode(self, value, currNode):
        if currNode.value == value:
            return currNode
        elif currNode.value > value and currNode.lChild != None:
            return self._findNode(value, currNode.lChild)
        elif currNode.value < value and currNode.rChild != None:
            return self._findNode(value, currNode.rChild)
        return None

    def search(self, value):
        return True if self.findNode(value) else False

    def delete(self, value):
        return self._delete(self.findNode(value))

    def _delete(self, node):
        if node == None or self.findNode(node.value) == None:
            print("Node is not found!")
            return

        def findMinNode(node):
            currNode = node
            if currNode.lChild == None:
                return currNode
            else:
                return findMinNode(currNode.lChild)

        def childrenNum(node):
            num = 0
            if node.rChild != None:
                num += 1
            if node.lChild != None:
                num += 1
            return num

        if node.freq > 1:
            node.freq -= 1
        else:
            nodeChildern = childrenNum(node)
            nodePerent = node.perent
            if nodeChildern == 0:
                if nodePerent != None:
                    if nodePerent.lChild == node:
                        nodePerent.lChild = None
                    else:
                        nodePerent.rChild = None
                else:
                    self.root = None
            if nodeChildern == 1:
                if node.lChild != None:
                    child = node.lChild
                else:
                    child = node.rChild
                if nodePerent != None:
                    if nodePerent.lChild == node:
                        nodePerent.lChild = child
                    else:
                        nodePerent.rChild = child
                else:
                    self.root = child
                child.perent = nodePerent
            if nodeChildern == 2:
                minChild = findMinNode(node.rChild)
                node.value = minChild.value
                self._delete(minChild)
                return
            if nodePerent != None:
                nodePerent.height = 1 + self.tallerChildHeight(nodePerent)
                self._delBalancing(nodePerent)

    def _insBalancing(self, currNode, path=[]):
        if currNode.perent == None:
            return
        path = [currNode] + path
        lHeight = self.getHeight(currNode.perent.lChild)
        rHeight = self.getHeight(currNode.perent.rChild)
        if abs(lHeight - rHeight) > 1:
            path = [currNode.perent] + path
            self._balanceTree(path[0], path[1], path[2])
            return
        newHeight = 1 + currNode.height
        if newHeight > currNode.perent.height:
            currNode.perent.height = newHeight
        self._insBalancing(currNode.perent, path)

    def _delBalancing(self, currNode):
        if currNode.perent == None:
            return
        lHeight = self.getHeight(currNode.lChild)
        rHeight = self.getHeight(currNode.rChild)
        if abs(lHeight - rHeight) > 1:
            b = self.tallerChild(currNode)
            c = self.tallerChild(b)
            self._balanceTree(currNode, b, c)

        self._delBalancing(currNode.perent)

    def _balanceTree(self, a, b, c):
        if b == a.lChild and c == b.lChild:
            self._rightRotate(a)
        elif b == a.lChild and c == b.rChild:
            self._leftRotate(b)
            self._rightRotate(a)
        elif b == a.rChild and c == b.rChild:
            self._leftRotate(a)
        elif b == a.rChild and c == b.lChild:
            self._rightRotate(b)
            self._leftRotate(a)
        else:
            raise Exception('Error in balancing')

    def getHeight(self, node):
        if node != None:
            return node.height
        return 0

    def tallerChildHeight(self, node):
        return max(self.getHeight(node.rChild), self.getHeight(node.rChild))

    def tallerChild(self, currNode):
        lHeight = self.getHeight(currNode.lChild)
        rHeight = self.getHeight(currNode.rChild)
        return currNode.lChild if lHeight > rHeight else currNode.rChild

    def _rightRotate(self, a):
        prePerent = a.perent
        y = a.lChild
        yRightChild = y.rChild
        y.rChild = a
        a.perent = y
        a.lChild = yRightChild
        y.perent = prePerent
        if yRightChild != None:
            yRightChild.perent = a
        if y.perent == None:
            self.root = y
        else:
            if y.perent.lChild == a:
                y.perent.lChild = y
            else:
                y.perent.rChild = y
        y.height = 1 + self.tallerChildHeight(y)
        a.height = 1 + self.tallerChildHeight(a)

    def _leftRotate(self, a):
        prePerent = a.perent
        y = a.rChild
        yLeftChild = y.lChild
        y.lChild = a
        a.perent = y
        a.rChild = yLeftChild
        y.perent = prePerent
        if yLeftChild != None:
            yLeftChild.perent = a
        if y.perent == None:
            self.root = y
        else:
            if y.perent.lChild == a:
                y.perent.lChild = y
            else:
                y.perent.rChild = y
        y.height = 1 + self.tallerChildHeight(y)
        a.height = 1 + self.tallerChildHeight(a)


y = [1,2,3,4,5]
print(y, "is a list")
y = AVLTree(y)
print(y, "is binarySearchTree")
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
print("{} {}".format("Searching for 1:\n", "Found!" if y.search(1) else "Not found!"))
y.delete(1)
print(y)
print("{} {}".format("Searching for 1:\n", "Found!" if y.search(1) else "Not found!"))
y.insert(0)
print(y)
print("{} {}".format("Searching for 0:\n", "Found!" if y.search(0) else "Not found!"))
print(y.height())
y.delete(0)
y.delete(2)
print(y.height())
y.delete(3)
print(y.height())
y.delete(4)
print(y.height())
print(y)
for i in range(1000):  # BST height issue  solved ^_^
    y.insert(i)
print(y)
print(y.height())