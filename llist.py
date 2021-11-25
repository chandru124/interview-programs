import math
 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 

def insert(root, item):
    temp = Node(item)
     
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
     
    return root
 
def display(root):
    while (root != None) :
        print(root.data, end = "-->")
        root = root.next
         
def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
     
    return root
 

if __name__=='__main__':
    str=input("enter the value")
    arr = str.split()
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)
     
