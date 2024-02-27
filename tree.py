#! /usr/bin/env python
from typing import Any, Optional


# Eine Node hat einen Wert, value
# und zwei "Zweige" left und right.
# Wenn die nicht angegeben sind, sind die None.

class Node:
    def __init__(self, value: Any, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        """ Return a string representation of the node. """
        left = "None"
        right = "None"
        if self.left is not None:
            left = self.left.value
        if self.right is not None:
            right = self.right.value

        # Was passiert, wenn wir stattdessen {self.left} und {self.right} einsetzen würden? → Rekursion (aber versteckt)
        return f"Node(value={self.value}, left={left}, right={right})"

    def preorder_walk(self):
        value = self.value
        print(f"{value}", end=' ')
        if self.left is not None:
            self.left.preorder_walk()
        if self.right is not None:
            self.right.preorder_walk()

    def inorder_walk(self):
        value = self.value

        if self.left is not None:
            self.left.inorder_walk()
        print(f"{value}", end=' ')
        if self.right is not None:
            self.right.inorder_walk()

    def postorder_walk(self):
        value = self.value
        if self.left is not None:
            self.left.postorder_walk()
        if self.right is not None:
            self.right.postorder_walk()
        print(f"{value}", end=' ')


class Lexer:
    def __init__(self, the_input: str):
        self.input = the_input
        self.words = [word.strip() for word in the_input.split()]

    def tokenize(self):
        for word in self.words:
            yield word


# 5 + 2 * 4
#
#    +
#   / \
#  5   *
#     / \
#    2   4

if __name__ == "__main__":
    n = Node('*')
    n.left = Node('2')
    n.right = Node('4')

    m = Node('+')
    m.left = Node('5')
    m.right = n

    m.preorder_walk()
    print()
    m.inorder_walk()
    print()
    m.postorder_walk()
    print()
