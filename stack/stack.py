"""Stack data structure, LIFO, more info in the class docstring."""
class Stack:
    """The stack is used in situations where the most recent value should be the first returned.
    This is called LIFO(Last In First Out), a real world example would be a stack of dishes,
    the bottom dish was put there first, and if new dishes are added they are added to the top.
    Sometimes I load new dishes to the bottom to give the bottom plates a chance to be used,
    but you don't do that with stacks,
    The methods associated with stacks are empty(), size(), top(), push(item), and pop()"""


    def __init__(self):

        self.items = []


    def empty(self):
        """Returns whether or not the stack is empty"""
        return self.items == []


    def size(self):
        """Returns the total amount of items in stack."""
        return len(self.items)


    def top(self):
        """Returns the value of the top item in the stack without removing."""
        return self.items[-1]


    def push(self, item):
        """Adds an item to the stack."""
        return self.items.append(item)


    def pop(self):
        """Removes the top item in the stack."""
        return self.items.pop()
