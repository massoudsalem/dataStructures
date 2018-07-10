# This binarySearchTree structure is written by Moh.Massoud in 06July18
class node:
    def __init__(self, key, value, d=False):
        self.key = key
        self.value = value
        self.deleted = d

    def __str__(self):
        return "{} : {}".format(self.key, self.value)


class HashTable:
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.list = [None] * self.capacity

    def _genStr(self):
        str = ""
        for i in self.list:
            if (i != None):
                str += "{} : {}, ".format(i.key, i.value)
        return str[:-2]

    def __str__(self):
        return "[" + self._genStr() + "]"
               # + "\nCapacity of HashTable is {}".format(self.capacity)

    def _hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return (((sum * 353) % 1000000007) * 23) % self.capacity

    def insert(self, key, value, notOperation=True):
        index = self._hash(key)
        while (self.list[index] != None and self.list[index].deleted != True):
            index += 1
        self.list[index] = node(key, value)
        if (notOperation):
            self.size += 1
        if (self.size >= self.capacity / 2 or index > self.capacity):
            self._doubleCapacity()
        elif (self.size * 4 < self.capacity):
            self._halfenCapacity()

    def _doubleCapacity(self):
        listCopy = self.list.copy()
        self.capacity = self.capacity * 2
        self.list = [None] * self.capacity
        for x in listCopy:
            if x != None:
                self.insert(x.key, x.value, False)

    def _halfenCapacity(self):
        listCopy = self.list.copy()
        self.capacity = self.capacity // 2
        self.list = [None] * self.capacity
        for x in listCopy:
            if x != None:
                self.insert(x.key, x.value, False)

    def find(self, key):
        idx = self._find(key)
        if (idx != -1):
            return self.list[idx]
        else:
            print("Node isn't found!")
            return -1

    def _find(self, key):
        index = self._hash(key)
        while (self.list[index] != None and self.list[index].key != key):
            index += 1
        if (self.list[index] != None and self.list[index].key == key):
            return index
        return -1

    def remove(self, key):
        idx = self._find(key)
        if (idx != -1):
            self.list[idx] = None
            self.size -= 1
            if (self.size * 4 < self.capacity):
                self._halfenCapacity()
        else:
            print("key is not found!!")

    def getValue(self, key):
        idx = self._find(key)
        if (idx != -1):
            return self.list[idx].value
        else:
            print("key is not found!!")


h = HashTable()
h.insert("map1", 1)
print(h)
h.insert("map2", 2)
print(h)
h.insert("map3", 3)
print(h)
h.insert("map4", 4)
print(h)
h.remove("map1")
print(h)
h.insert("map1", 1)
print(h)
h.insert("map5", 5)
print(h)
h.insert("map6", 6)
print(h.getValue("map5"))
print(h)
h.remove("map7")
print(h)
h.remove("map5")
print(h)
h.remove("map2")
print(h)
h.remove("map1")
print(h)
h.remove("map6")
print(h)
h.remove("map3")
print(h)
h.remove("map4")
print(h)
print(h.getValue("map8"))
