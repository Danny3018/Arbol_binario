from binarytree import Node

root = Node(25)
#Primer nivel 
root.right = Node(36)
root.left= Node(20)

#Segundo nivel 
root.right.left= Node(30)
root.right.right= Node(40)
root.left.right= Node(22)
root.left.left= Node(10)

# Tercer nivel 
root.right.right.right= Node(48)
root.right.right.left= Node(38)
root.right.left.left= Node(28)
root.left.left.right= Node(12)
root.left.left.left= Node(5)


#Cuarto nivel 
root.right.right.right.right= Node(50)
root.right.right.right.left= Node(45)
root.left.left.right.right= Node(15)
root.left.left.left.right= Node(8)
root.left.left.left.left= Node(1)



print(root)

print("1) La altura del arbol es:", root.height)
print("2) Las hojas son:", root.leaves)
print("3) La cantidad de hojas  que posee el arbol son:", root.leaf_count)
print("4) Los niveles del arbol son:", root.levels)
print("5) El tamaño del arbol es:", root.size)
