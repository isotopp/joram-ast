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


class Lexer:
    def __init__(self, the_input: str):
        self.input = the_input
        self.words = [word.strip() for word in the_input.split()]

    def tokenize(self):
        for word in self.words:
            yield word


if __name__ == "__main__":
    l = Lexer("5 + 2 * 4 + 6")
    print(f"{l.words}")
    for word in l.tokenize():
        print(f"{word=}")
