import math
class Node:
    
    def __init__(self, data):         
        self.data = data
        self.next = None

class LinkedList:
     
    def __init__(self):     
        self.head = None
 

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
          print(root.data, end = " ")
          root = root.next

    def arrayToList(arr, n):
      root = None
      for i in range(0, n, 1):
        root = LinkedList.insert(root, int(arr[i]))

      return root
 

    def reverse(Head):
     
     if (Head is None and
        Head.next is None):
        return Head
         
     prev = None
     curr = Head
     
     while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
         
     Head = prev
     return Head
 
    def addTwoNumbers(l1, l2):
        
       if l1 is None:
        return l1
       if l2 is None:
        return l2
       l1 = LinkedList.reverse(l1)
       l2 = LinkedList.reverse(l2)
       head = l1
       prev = None
       c = 0
       sum = 0
     
       while l1 is not None and l2 is not None:
          sum = c + l1.data + l2.data
          l1.data = sum % 10
          c = int(sum / 10)
          prev = l1
          l1 = l1.next
          l2 = l2.next
       if l1 is not None or l2 is not None:
            if l2 is not None:
               prev.next = l2
            l1 = prev.next
         
            while l1 is not None:
             sum = c + l1.data
             l1.data = sum % 10
             c = int(sum / 10)
             prev = l1
             l1 = l1.next
             
       if c > 0:
            prev.next = Node(c)
         
       return LinkedList.reverse(head)
            


if __name__=='__main__':
    str1 = input("enter the 1list")
    str2 = input("enter the 2 list")
    arr1 = str1.split()
    arr2 = str2.split()
    n1 = len(arr1)
    n2 = len(arr2)
    root1 = LinkedList.arrayToList(arr1, n1)
    root2 = LinkedList.arrayToList(arr2, n2)

    add=LinkedList.addTwoNumbers(root1,root2)
    LinkedList.display(add)
    
      
