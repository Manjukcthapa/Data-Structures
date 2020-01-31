import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
  # check if the new node's value is less than
      # is there a child? If not insert new node
      #  otherwise repeat the process
    # check if new node's value is greater than
      # is there a child? if not insert new node
      # otherwise repeat the process

       # if inserting, there must be a root
        # if value is < self.value
      if value < self.value:
            # if not keep going
            if self.left is None:
                self.left = BinarySearchTree(value)
            # make a left node
            else:
                self.left.insert(value)
        # if >= then go right and
      elif value >= self.value:
            # if not keep going
            if self.right is None:
                self.right = BinarySearchTree(value)
            # make a new node
            else:
                self.right.insert(value)

 # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass 
    #if target is the self.value
        if target == self.value:
     #return true       
         return True
     # elif self.right is none and self.left    
        elif self.right is None and self.left:
     #return false
         return False
      #if not return false   
        else:
      #  if self.left and if self.left.contain target return true     
         if self.left:
          if self.left.contains(target):
           return True
       #if self.right and if self.right.contain target returen true    
        if self.right:
         if self.right.contains(target):
          return True
            


    # Return the maximum value found in the tree
    def get_max(self):
    
    ## if we have a right
     if self.right:
      ## return right's get max
      return self.right.get_max()
    ## otherwise, return self.value
     else:
      return self.value
    


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
         # call the callback on the self's value
     cb(self.value)
    # if self.right
     if self.right:
      ## call rightie's for_each with the cb
      self.right.for_each(cb)
    # if self.left
     if self.left:
      ## leftie's for_each with the cb
      self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            in_order_print(self.left)
            print(self.value)
            in_order_print(self.right)

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

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
