# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:04:47 2024

@author: danid
"""

# constructor

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    # start the tree with no root. Insert 
    def __init__(self):
        self.root = None
        
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        
        while True:
            # if duplicate
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value):
        
        # not really needed
        # if self.root == None:
        #     return False
        
        temp = self.root
        
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            
            elif value > temp.value:
                temp = temp.right
            
            else:
                return True
            
        return False       
        
    
        
mytree = BinarySearchTree()
print(mytree.root)
mytree.insert(3)
mytree.insert(5)
mytree.insert(2)
print(mytree.root.value)
print(mytree.root.left.value)
print(mytree.root.right.value)
print(mytree.contains(7))
mytree.contains(2)











        
        
        