from binarytree import Node

root = Node(100)
#Primer nivel 
root.right = Node(36)
root.left= Node(19)

#Segundo nivel 
root.right.left= Node(25)
root.right.right= Node(1)
root.left.right= Node(3)
root.left.left= Node(17)

# Tercer nivel 
root.left.left.right= Node(7)
root.left.left.left= Node(2)



print(root)

print("1) La altura del arbol es:", root.height)
print("2) Las hojas son:", root.leaves)
print("3) La cantidad de hojas  que posee el arbol son:", root.leaf_count)
print("4) Los niveles del arbol son:", root.levels)
print("5) El tamaño del arbol es:", root.size)
