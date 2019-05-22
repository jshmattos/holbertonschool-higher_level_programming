#!/usr/bin/python3


class Node():
    """A Node class."""

    def __init__(self, data, next_node=None):
        """Initialize class."""
        self.data = data
        self.next_node = next_node

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
        if value is None:
            self.__next_node = value
            return
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """A singly linked list class."""

    def __init__(self):
        """Initialize class."""
        self.__head = None
        self.__size = 0

    def sorted_insert(self, value):
        """Inserts a node according to its sorted value."""
        new_node = Node(value)
        # print("current Node is " + str(new_node.data))
        # list is empty
        if self.__head is None:
            # print("list is empty")
            new_node.next_node = self.__head
            self.__head = new_node
            self.__size += 1
            return
        if value < self.__head.data:
            # print("need to insert to begin")
            new_node.next_node = self.__head
            self.__head = new_node
            self.__size += 1
            return
        curr = self.__head
        while value >= curr.data:
            # print("comparing..")
            # print(str(value) + ", " + str(curr.data))
            prev = curr
            if curr.next_node:
                curr = curr.next_node
            else:
                # reached end
                # print("reached end")
                curr.next_node = new_node
                new_node.next_node = None
                return
        # print("time to add..")
        # print("current value is " + str(curr.data))
        prev.next_node = new_node
        new_node.next_node = curr

    def print_list(self):
        curr = self.__head
        while curr is not None:
            print(curr.data)
            curr = curr.next_node

    def __str__(self):
        string = ""
        curr = self.__head
        if curr == None:
            return ""
        while curr is not None:
            string += str(curr.data)
            string += "\n"
            curr = curr.next_node
        return string[:-1]
