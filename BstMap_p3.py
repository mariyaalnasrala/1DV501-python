from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    key: Any = None
    value: Any = None
    left: Any = None
    right: Any = None

    def add(self, key, value):
        if self.key == key:
            self.value = value
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.add(key, value)
        else:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.add(key, value)

    def to_string(self):
        res = ''
        if self.left is not None:
            res += self.left.to_string() + " "
        res += f"({self.key}, {self.value})"
        if self.right is not None:
            res += " " + self.right.to_string()
        return res
    
    def get(self, key):
        if self.key == key:
            return self.value
        elif key < self.key and self.left is not None:
            return self.left.get(key)
        elif key > self.key and self.right is not None:
            return self.right.get(key)
        else:
            return None

    def count(self):
        count = 1
        if self.left is not None:
            count += self.left.count()
        if self.right is not None:
            count += self.right.count()
        return count

    def max_depth(self):
        if self.left is not None:
            left_max_depth = self.left.max_depth()
        else:
            left_max_depth = 0
        if self.right is not None:
            right_max_depth = self.right.max_depth()
        else:
            right_max_depth = 0
        return max(left_max_depth, right_max_depth) + 1

    def inter_nodes(self):
        count = 0
        if self.left is not None or self.right is not None:
            count += 1
        if self.left is not None:
            count += self.left.inter_nodes()
        if self.right is not None:
            count += self.right.inter_nodes()
        return count

    def as_list(self, lst):
        if self.left is not None:
            self.left.as_list(lst)
        lst.append((self.key, self.value))
        if self.right is not None:
            self.right.as_list(lst)
        return lst


@dataclass
class BstMap_p3:
    root: Node = None

    def add(self, key, value):
        if self.root is None:
            self.root = Node(key, value, None, None)
        else:
            self.root.add(key, value)

    def to_string(self):
        if self.root is None:
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    def inter_nodes(self):
        if self.root is None:
            return 0
        else:
            return self.root.inter_nodes()

    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
