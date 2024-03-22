#!/usr/bin/env python
# coding: utf-8

# 16. If the following values were inserted into a min heap with an array implementation, what would the contents of the array contain?
# 
# 10 20 40 30 15 25 5 50 35 45
# 
# 

# In[ ]:


[5, 15, 10, 30, 20, 40, 25, 50, 35, 45]


# ![BST](practice-exam-bst.png)
# 

# 17. Write the order of nodes traveresed in the graph above for:

# * preorder 

# In[ ]:


20 10 70 60 50 90 80 100 110


# * inorder

# In[ ]:


10 20 50 60 70 80 90 100 110


# * postorder

# In[ ]:


10 50 60 80 110 100 90 70 20


# * level order

# 20 10 70 60 90 50 80 100 110

# 18. Write a function that accepts a linked list and verifies whether it is a palindrome or not. A palindrome is sequence of values that reads the same forward and backward (e.g. 1 2 3 4 3 2 1 and 0 2 0)

# In[ ]:


from dsa.singlylinkedlist import Node, LinkedList

def is_palindrome(ll):
    stack = []
    
    current = ll.head
    while current:
        stack.append(current.value)
        current = current.next

    current = ll.head
    count = len(stack) // 2
    
    while count > 0:
        sv = stack.pop()
        if current.value != sv:
            return False
        current = current.next
        count -= 1
    
    return True



# In[ ]:


ll = LinkedList()
print(ll, " palindrome? ", is_palindrome(ll))

ll = LinkedList.from_array([1])
print(ll, " palindrome? ", is_palindrome(ll))

ll = LinkedList.from_array([1, 1, 3, 3, 1, 1])
print(ll, " palindrome? ", is_palindrome(ll))

ll = LinkedList.from_array([1, 2, 2, 2, 1, 3, 3, 2, 1])
print(ll, " palindrome? ", is_palindrome(ll))


# solution with doubly linked lists

# In[ ]:


from dsa.doublylinkedlist import Node, DoublyLinkedList

def is_palindrome(dll):
    if not dll.head:
        return True

    left = dll.head
    right = dll.tail

    while left != right and left.prev != right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev

    return True


# In[ ]:


dll = DoublyLinkedList()
print(dll, " palindrome? ", is_palindrome(dll))

dll = DoublyLinkedList.from_array([1])
print(dll, " palindrome? ", is_palindrome(dll))

dll = DoublyLinkedList.from_array([1, 1, 3, 3, 1, 1])
print(dll, " palindrome? ", is_palindrome(dll))

dll = DoublyLinkedList.from_array([1, 2, 2, 2, 1, 3, 3, 2, 1])
print(dll, " palindrome? ", is_palindrome(dll))



# 19. Write a function that accepts a binary tree and returns its height.
# 
# 

# In[4]:


from dsa.tree import Tree, Node

def tree_height(root):
    if root is None:
        return 0
    
    left_depth = tree_height(root.left)
    right_depth = tree_height(root.right)
    
    return max(left_depth, right_depth) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
t = Tree(root)

print("Height:", tree_height(t.root)) 


# 20. Write a function that accepts a valid binary search tree and a number (n) and returns the nth largest number in the tree.
# 

# In[ ]:


from dsa.tree import Tree, Node

def inorder_traversal(root, result):
    if root is None:
        return
    inorder_traversal(root.right, result)
    result.append(root.value)
    inorder_traversal(root.left, result)

def nth_largest_in_bst(root, n):
    if root is None or n <= 0:
        return None
    
    result = []
    inorder_traversal(root, result)
    
    if n <= len(result):
        return result[n - 1]
    else:
        return None

root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(9)
t = Tree(root)

n = 3
nth_largest = nth_largest_in_bst(t.root, n)
if nth_largest is not None:
    print(f"The #{n} largest number is: {nth_largest}")
else:
    print(f"No #{n} largest number found.")


# 21. Write a function that given a starting vertex in a graph, returns the vertex with the most incoming edges. Implement for either an adjacency list or adjacency matrix representation.

# adjacency list solution

# In[ ]:


from dsa.graph import Vertex

def vertex_incoming_edges(vertex, visited={}, max_edges=0, max_vertex=None):
    visited[vertex] = True
    incoming_edges = len(vertex.adjacents)
    if incoming_edges > max_edges:
        max_edges = incoming_edges
        max_vertex = vertex
    
    for v in vertex.adjacents:
        if not visited.get(v, False):
            max_vertex = vertex_incoming_edges(v, visited, max_edges, max_vertex)

    return max_vertex
    

# Undirected Graph
# B has most incoming vertices (4)
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")

a.add_adjacent_vertex(b)
a.add_adjacent_vertex(c)
b.add_adjacent_vertex(c)
b.add_adjacent_vertex(e)
d.add_adjacent_vertex(b)
e.add_adjacent_vertex(d)
e.add_adjacent_vertex(f)

vertex_incoming_edges(a)


# adjacency matrix solution

# In[ ]:


from dsa.graph import AdjacencyMatrixGraph

def vertex_incoming_edges(graph):
    num_vertices = len(graph.array)
    incoming_edges = [0] * num_vertices

    for row in graph.array:
        for col, value in enumerate(row):
            if value:
                incoming_edges[col] += 1

    max_incoming_edges = max(incoming_edges)
    vertex_max = graph.labels[incoming_edges.index(max_incoming_edges)]

    return vertex_max

# undirected graph
# B has the most incoming edges (4)
graph = AdjacencyMatrixGraph(["A", "B", "C", "D", "E", "F"])
graph.add_adjacent_vertex("A", "B")
graph.add_adjacent_vertex("A", "C")
graph.add_adjacent_vertex("B", "C")
graph.add_adjacent_vertex("B", "E")
graph.add_adjacent_vertex("D", "B")
graph.add_adjacent_vertex("E", "D")
graph.add_adjacent_vertex("E", "F")

graph.print_graph()

vertex = vertex_incoming_edges(graph)
print(f"Vertex with the most incoming edges: {vertex}")


# In[ ]:




