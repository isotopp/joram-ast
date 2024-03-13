#! /usr/bin/env python
import re
import sys
from dataclasses import dataclass, field
from typing import Any, Optional, Generator

DEBUG = True

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
        if self.left is not None:
            self.left.postorder_walk()
        if self.right is not None:
            self.right.postorder_walk()
        print(f"{self.value}", end=' ')

    def postorder_apply(self, fn):
        if self.left is not None:
            self.left.postorder_apply(fn)
        if self.right is not None:
            self.right.postorder_apply(fn)
        fn(self)


def ausrechnen(node, indent=0):
    dent = "  " * indent
    if DEBUG: print(f"{dent}before {node=}")
    if node.left is not None:
        ausrechnen(node.left, indent+1)
    if node.right is not None:
        ausrechnen(node.right, indent+1)

    if node.value == '+':
        if node.left is None or node.right is None:
            raise RuntimeError(f"In {node}, found a none in {node.left=}, {node.right=}")

        node.value = node.left.value + node.right.value
        node.left = None
        node.right = None

    if node.value == '*':
        if node.left is None or node.right is None:
            raise RuntimeError(f"In {node}, found a none in {node.left=}, {node.right=}")

        node.value = node.left.value * node.right.value
        node.left = None
        node.right = None

    try:
        node.value = int(node.value)
    except ValueError:
        pass
    if DEBUG: print(f"{dent}after  {node=}")


@dataclass(frozen=True, slots=True)
class Token:
    type: Any
    value: Any
    line: int = field(default=None, compare=False)
    column: int = field(default=None, compare=False)


class Lexer:
    def __init__(self, the_input: str):
        self.input = the_input
        self.len = len(self.input)

        self.offset = 0
        self.line = 0
        self.column = 0

    def tokenize(self) -> Generator[Token, None, None]:
        NUMBER = re.compile(r"(-?\d+)", re.ASCII)
        OPERATOR = ['+', '*']

        while self.offset < self.len:
            c = self.input[self.offset]

            if c == '\n':
                self.line += 1
                self.offset += 1
                self.column = 0
                yield Token(type='EOL', value='\n', line=self.line, column=self.column)
            elif c.isspace():
                self.offset += 1
                self.column += 1
            elif m := re.match(NUMBER, self.input[self.offset:]):
                self.offset += len(m[0])
                self.column += len(m[0])
                yield Token(type='NUMBER', value=int(m[0]), line=self.line, column=self.column)
            elif c in OPERATOR:
                self.offset += 1
                self.column += 1
                yield Token(type='OPERATOR', value=c, line=self.line, column=self.column)
            else:
                self.offset += 1
                self.column += 1
                yield Token(type='char', value=c, line=self.line, column=self.column)

        self.offset += 1
        self.column += 1
        yield Token(type='EOF', value='\n', line=self.line, column=self.column)


class Parser:
    def __init__(self):
        pass

# 51 + 2 * 4
#
#    +
#   / \
#  51  *
#     / \
#    2   4
#

if __name__ == "__main__":
    expr = "51 + 2 * 4"
    l = Lexer(expr)
    for i in l.tokenize():
        print(f"{i} {l.offset} {l.line=} {l.char=}")
