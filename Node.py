'''
Created on Aug 25, 2018

@author: Dan Valinotti
'''
from sys import argv

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
        
class LinkedList:
    
    #Class definition
    def __init__(self, value):
        self.first = Node(value)
        self.length = 1
    
    #Traverses to node at (value) location and returns Node
    def traverse(self, value):
        r = None
        if self.length == 1:
            r = self.first
        else:
            value -= 1
            current = self.first
            for x in range(0, value):
                current = current.next
            r = current
        return r

    def __str__(self):
        current = self.first
        r = ''
        while current is not None:
            r = r + str(current.value) + ' '
            current = current.next
        return r
    
    def add(self, value):
        last = self.traverse(self.length)
        last.next = Node(value)
        self.length += 1
    
    def returnLast(self):
        print(self.traverse(self.length))
        return self.traverse(self.length)