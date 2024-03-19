import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(node, visited=None):    
    if visited is None:
        visited = set()
    if node not in visited:
        visited.add(node)
        colors = ['#800080', '#FF0000', '#FFA500', '#FFFF00', '#008000', '#0000FF']  # Кольори відповідно до порядку обходу, індекс починається з 1 і закінчується 0, тому зсунув 1 колір
        color_index = len(visited) % len(colors)            
        node.color = colors[color_index]
        if node.left:
            dfs(node.left, visited)
        if node.right:
            dfs(node.right, visited)


def bfs(node):
    visited = set()
    queue = [node]
    colors = ['#FF0000', '#FFA500', '#FFFF00', '#008000', '#0000FF', '#800080']  # Кольори відповідно до порядку обходу
    color_index = 0
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.add(current_node)
            current_node.color = colors[color_index]
            color_index = (color_index + 1) % len(colors)  # Змінюємо індекс кольору для наступного вузла
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в глибину
dfs(root)
draw_tree(root)

# Обхід в ширину
bfs(root)
draw_tree(root)
