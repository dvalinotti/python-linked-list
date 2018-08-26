'''
Created on Aug 25, 2018

@author: Dan Valinotti
'''

import Node

def bubbleSort (list):
    current = list.first
    if current.next == None:
        return list
    else:
        sorted = False
        while not sorted:
            sorted = True
            previous = list.first
            current = previous.next
            while current != None:
                if previous.value > current.value:
                    sorted = False
                    temp = previous.value
                    previous.value = current.value
                    current.value = temp
                
                if current != None:
                    previous = current
                    current = current.next
    print(list)
    
def insertionSort (list):
    return None
def mergeSort (list):
    return None