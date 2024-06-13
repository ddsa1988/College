from BinarySearchTree import BST
from Person import Person

tree = BST()

# p1 = Person("Diego", 10)
# p2 = Person("Amanda", 20)
# p3 = Person("Rodrigo", 30)
# p4 = Person("Caio", 40)
# p5 = Person("Zeus", 50)
# 
# tree.insert(p1)
# tree.insert(p2)
# tree.insert(p3)
# tree.insert(p4)
# tree.insert(p5)

tree.insert(11)
tree.insert(7)
tree.insert(15)
tree.insert(5)
tree.insert(3)
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(13)
tree.insert(12)
tree.insert(14)
tree.insert(20)
tree.insert(18)
tree.insert(25)
tree.insert(6)


def print_node(value):
    print(value, end=" ")


print("In-order: ", end=" ")
tree.in_order_traverse(print_node)

# print("\nPre-order: ", end=" ")
# tree.pre_order_traverse(print_node)
#
# print("\nPost-order: ", end=" ")
# tree.post_order_traverse(print_node)
#
# print()
# print(f"Min: {tree.min()}")
# print(f"Max: {tree.max()}")
#
# print(tree.search(18))
# print(tree.search(100))

tree.remove(13)
print()
print("In-order: ", end=" ")
tree.in_order_traverse(print_node)
