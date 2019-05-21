#!/usr/bin/python3


class Node():
    """A Node class."""

    def __init__(self, data, next_node=None):
        """Initialize class."""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None or isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve data at Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set value of Node class"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set value of next Node."""
        # if not isinstance(value, Node) or value != None:
        #   raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """A singly linked list class."""

    def __init__(self):
        """Initialize class."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node according to its sorted value."""
        new_node = Node(value)
        # empty list
        if self.__head is None:
            self.__head = new_node
            self.next_node = None
            return
        curr = self.__head
        while curr is not None:
            print(curr.data)
            if value >= curr.data:
                curr.next_node = new_node
                if curr.next_node is not None:
                    new_node.next_node = curr.next_node
                else:
                    curr.next_node = None
                break
            curr = curr.next_node
        """
        current = self.__head
        new_node.next_node = current
        self.__head = new_node
        """

    def print_list(self):
        current = self.__head
        while current is not None:
            print(current.data)
            current = current.next_node
