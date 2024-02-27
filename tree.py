#! /usr/bin/env python

# Eine Node hat einen Wert, value
# und zwei "Zweige" left und right.
# Wenn die nicht angegeben sind, sind die None.

class Node:
    def __init__(self, value, left=None, right=None):
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

        # Was passiert, wenn wir stattdessen {self.left} und {self.right} einsetzen würden? -> Rekursion (aber versteckt)
        return f"Node(value={self.value}, left={left}, right={right})"


if __name__ == "__main__":
    # Wir machen uns eine einsame Node n
    n = Node(1)
    print(f"{n=}")

    # Wir machen uns Nodes l und r und weisen sie n.left und n.right nachträglich zu
    l = Node(2)
    r = Node(3)
    n.left = l
    n.right = r
    print(f"{n=}")

    # Dasselbe in einem Arbeitsgang
    all = Node(1, Node(2), Node(3))
    print(f"{all=}")
