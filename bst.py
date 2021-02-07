class Node():
    def __init__(self, key, val, left=None, right=None, parent=None, height=1):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def add(self, key, val):
        if key > self.key:
            if self.right == None:
                self.right = Node(key, val, parent=self)
                self.update_height()
            else:
                self.right.add(key, val)
        else:
            if self.left == None:
                self.left = Node(key, val, parent=self)
                self.update_height()
            else:
                self.left.add(key, val)

    def remove(self, key):
        node = self.search(key)
        if node.left == None and node.right == None:
            if node.key > node.parent.key:
                node.parent.right = None
            else:
                node.parent.left = None
            if node.parent != None:
                node.parent.update_height()
        elif node.right == None:
            if node.key > node.parent.key:
                node.parent.right = node.left
                node.parent.right.parent = node.parent
            else:
                node.parent.left = node.left
                node.parent.left.parent = node.parent
            if node.parent != None:
                node.parent.update_height()
        elif node.left == None:
            if node.key > node.parent.key:
                node.parent.right = node.right
                node.parent.right.parent = node.parent
            else:
                node.parent.left = node.right
                node.parent.left.parent = node.parent
            if node.parent != None:
                node.parent.update_height()
        else:
            new_key = node.find_le(node.key-1)
            node_mv = node.search(new_key)
            node.key = new_key
            if node_mv.left == None:
                node_mv.parent.right = None
                node_mv.parent.update_height()
            else:
                node_mv.parent.right = node_mv.left
                node_mv.parent.right.parent = node_mv.parent


    def get(self, key):
        if key > self.key:
            return self.right.get(key)
        elif key < self.key:
            return self.left.get(key)
        else:
            return self.val

    def search(self, key):
        if key > self.key:
            return self.right.search(key)
        elif key < self.key:
            return self.left.search(key)
        else:
            return self

    def print_tree(self, tab=0):
        if (self.left != None): self.left.print_tree(tab + 2)
        print(tab * " " + str(self.key))
        if (self.right != None): self.right.print_tree(tab + 2)

    def iterate(self, arr):
        if (self.left != None): self.left.iterate(arr)
        arr.append(self.key)
        if (self.right != None): self.right.iterate(arr)

    def get_height(self):
        return self.height

    def update_height(self):
        no_upd = self.height
        if self.left == None and self.right == None:
            self.height = 1
        elif self.left == None:
            self.height = self.right.height+1
        elif self.right == None:
            self.height = self.left.height+1
        else:
            self.height = max(self.left.height, self.right.height)+1
        if no_upd != self.height and self.parent != None:
            self.parent.update_height()

    def count_height(self):
        if self.left == None and self.right == None:
            self.height = 1
        elif self.left == None:
            self.height = self.right.count_height()+1
        elif self.right == None:
            self.height = self.left.count_height()+1
        else:
            self.height = max(self.left.count_height(), self.right.count_height())+1
        return self.height

    def print_height(self, tab=0):
        if self.left != None:
            self.left.print_height(tab+2)
        print(tab*" ", self.height)
        if self.right != None:
            self.right.print_height(tab+2)

    def find_ge(self, key):
        if key > self.key:
            if self.right == None:
                parent = self.parent
                while parent.key < key:
                    parent = parent.parent
                    if parent.parent == None:
                        return None
                return parent.key
            return self.right.find_ge(key)
        elif key < self.key:
            if self.left == None:
                return self.key
            else:
                return self.left.find_ge(key)
        else:
            return self.key

    def find_le(self, key):
        if key < self.key:
            if self.left == None:
                parent = self.parent
                while parent.key > key:
                    parent = parent.parent
                    if  parent.parent == None:
                        return None
                return parent.key
            return self.left.find_le(key)
        elif key > self.key:
            if self.right == None:
                return self.key
            else:
                return self.right.find_le(key)
        else:
            return self.key

    def range(self, left, right, arr, up=0, down=0, flag=0):
        if flag:
            key_left = self.find_ge(left)
            key_right = self.find_le(right)
            node = self.search(key_left)
            node.range(left, right, arr)
        else:
            if up != 1 and self.key > left and self.left != None:
                self.left.range(left, right, arr, down=1)
            if self.key <= right and self.key >= left:
                arr.append(self.key)
            if up != 2 and self.key < right and self.right != None:
                self.right.range(left, right, arr, down=2)
            if not down and self.parent != None:
                if self.parent.key > self.key:
                    self.parent.range(left, right, arr, up=1)
                else:
                    self.parent.range(left, right, arr, up=2)


root = Node(10, 1010)
root.add(5, 55)
root.add(3, 33)
root.add(8, 88)
root.add(2, 22)
root.add(4, 44)
root.add(1, 11)
root.add(7, 77)
root.add(9, 99)
root.add(6, 66)
root.add(15, 1515)
root.add(13, 1313)
root.add(19, 1919)
root.add(11, 1111)
root.add(14, 1414)
root.add(12, 1212)
root.add(18, 1818)
root.add(20, 2020)
root.add(17, 1717)
root.add(16, 1616)
root.remove(10)
root.remove(7)
root.remove(11)
root.remove(16)
root.print_tree()

iter_arr = []
root.iterate(iter_arr)
print(iter_arr)

range_arr = []
root.range(5, 16, range_arr, flag=1)
print(range_arr)

print(root.search(4).key)
print(root.get(4))

print(root.get_height())
root.print_height()
print('\n\n')
root.count_height()
root.print_height()

