from main.Node import LinkedList
from main.Sorting import bubbleSort
#Define test linked list
l = LinkedList(4)

#print(l)

#Add first and second nodes
l.add(5)
#print(l)
l.add(2)
#print(l)
l.add(1)

#Print last item in linked list
#l.returnLast()
print(l)
bubbleSort(l)