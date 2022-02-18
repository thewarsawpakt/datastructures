from __future__ import annotations
import typing


class binaryTreeNode:
    def __init__(self, data: typing.Any, left: typing.Union[binaryTreeNode, None],
                 right: typing.Union[binaryTreeNode, None]) -> None:
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def traverse(head: binaryTreeNode) -> None:
        if head.left:
            binaryTreeNode.traverse(head.left)
        print(f"{head.data}")
        if head.right:
            binaryTreeNode.traverse(head.right)

    @staticmethod
    def lookup(head: binaryTreeNode, value: typing.Any) -> typing.Union[binaryTreeNode, bool]:
        if head.data == value:
            return head

        if head.data > value:
            if head.left is None:
                return False
            return binaryTreeNode.lookup(head.left, value)
        if head.data < value:
            if head.right is None:
                return False
            return binaryTreeNode.lookup(head.right, value)

    @staticmethod
    def insert(self, head: binaryTreeNode, data: typing.Any) -> None:

        if data < head.data:
            if head.left:
                binaryTreeNode.insert(head.left, data)
            else:
                head.left = binaryTreeNode(data, None, None)

        elif data > head.data:
            if head.right:
                binaryTreeNode.insert(head.right, data)
            else:
                head.right = binaryTreeNode(data, None, None)
