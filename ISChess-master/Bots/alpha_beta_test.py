
from Node import Node

def minimax(node, depth=3, maximizingPlayer=True, alpha = float('-inf'), beta = float('inf')):
    if node.is_leaf() or depth == 0:
        return node.value
    if maximizingPlayer:
        max_evaluation = float('-inf')
        for child in node.children:
            evaluation = minimax(child, depth - 1, alpha, beta, False)
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, max_evaluation)
            if beta <= alpha:
                break
        return max_evaluation

    else:
        min_evaluation = float('inf')
        for child in node.children:
            evaluation = minimax(child, depth - 1, alpha, beta, True)
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, min_evaluation)
            if beta <= alpha:
                break
        return min_evaluation

root = Node(1)

# Livello 1
root.add_child(Node(2))
root.add_child(Node(3))

# Nodi del Livello 2
node_2 = root.find_child(2)
node_3 = root.find_child(3)

node_2.add_child(Node(4))
node_2.add_child(Node(5))
node_3.add_child(Node(6))

# Nodi del Livello 3
node_4 = node_2.find_child(4)
node_5 = node_2.find_child(5)
node_6 = node_3.find_child(6)

node_4.add_child(Node(7))
node_4.add_child(Node(8))
node_5.add_child(Node(9))
node_6.add_child(Node(10))

# Stampa dell'albero
root.print_tree(1)

a = minimax(root)
print(a)