from __future__ import annotations
import typing


class linkedListNode:
    def __init__(self, _next: linkedListNode, value: typing.Any) -> None:
        self.next = _next
        self.value = value

    def __next__(self) -> linkedListNode:
        if self.next:
            return self.next
        else:
            raise StopIteration

    def __repr__(self) -> str:
        return f'<linkedListNode next={self.next} value={self.value}>'

    @staticmethod
    def search(node: linkedListNode, value: typing.Any) -> typing.Union[None, linkedListNode]:
        if not node:
            return None
        if node.value == value:
            return node
        else:
            return linkedListNode.search(node.next, value)

    @staticmethod
    def insert(node: linkedListNode, value: typing.Any) -> linkedListNode:
        old_next = node.next
        new_node = linkedListNode(linkedListNode, value)
        node.next = new_node

        return node
