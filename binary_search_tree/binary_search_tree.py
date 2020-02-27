import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    # insert value
# if no root insert value as root
# compare value to root
# if value is smaller
#   look left if node repeat steps
#   if no node make new one with this value
# if value is larger or equal
#   look right, if node repeat steps.
#   if no node make new one with this value


    def insert(self, value):
        if value < self.value:
            if self.left == None: 
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    # IS FIND PSUDO CODE

# Find value
# if no node at root
#   return false
# Compare value to root
# if smaller
#   go left look at node 
#  if larger or ==
#       go right


    def contains(self, target):
        if self.value == None:
            return False
        if target == self.value:
            return True
        if target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        if target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

#Get max

    def get_max(self):
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
