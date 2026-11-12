from collections import deque


# ==========================================
# 1. BINARY TREE IMPLEMENTATION & TRAVERSALS
# ==========================================
class TreeNode:

    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def build_binary_tree():
    # Constructing Binary Tree for COLONGON
    root = TreeNode("C")
    root.left = TreeNode("O")
    root.right = TreeNode("L")

    root.left.left = TreeNode("O")
    root.left.right = TreeNode("N")
    root.right.left = TreeNode("G")
    root.right.right = TreeNode("O")

    root.left.left.left = TreeNode("N")
    return root


def binary_tree_bfs(start_node):
    if not start_node:
        return []
    visited = []
    queue = deque([start_node])
    while queue:
        current = queue.popleft()
        visited.append(current.label)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return visited


def binary_tree_dfs(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node.label)
        if node.label == "L":
            binary_tree_dfs(node.right, visited)
            binary_tree_dfs(node.left, visited)
        else:
            binary_tree_dfs(node.left, visited)
            binary_tree_dfs(node.right, visited)
    return visited


def run_binary_tree():
    print("\n--- Running Binary Tree Traversals ---")
    root = build_binary_tree()
    bfs_result = binary_tree_bfs(root)
    dfs_result = binary_tree_dfs(root)

    print("BFS Result:", " - ".join(bfs_result))
    print("DFS Result:", " - ".join(dfs_result))


# ==========================================
# 2. GRAPH IMPLEMENTATION & TRAVERSALS
# ==========================================
# Unique IDs mapped to display letters for COLONGON graph
labels = {
    "C1": "C",
    "O1": "O",
    "O2": "O",
    "N1": "N",
    "N2": "N",
    "L1": "L",
    "G1": "G",
    "O3": "O",
}

graph_bfs_adj = {
    "C1": ["O1", "O2", "N1"],
    "O1": ["L1", "G1"],
    "O2": ["N2"],
    "N1": [],
    "N2": [],
    "L1": [],
    "G1": ["O3"],
    "O3": [],
}

graph_dfs_adj = {
    "C1": ["O1", "O2", "N1"],
    "O1": ["G1", "L1"],
    "G1": ["O3"],
    "O3": [],
    "L1": [],
    "O2": ["N2"],
    "N2": [],
    "N1": [],
}


def graph_bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(labels[vertex])
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def graph_dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(labels[start])
    for neighbor in graph[start]:
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited, order)
    return order


def run_graph():
    print("\n--- Running Graph Traversals ---")
    bfs_result = graph_bfs(graph_bfs_adj, "C1")
    dfs_result = graph_dfs(graph_dfs_adj, "C1")

    print("BFS Result:", " - ".join(bfs_result))
    print("DFS Result:", " - ".join(dfs_result))


# ==========================================
# MAIN MENU FUNCTION
# ==========================================
def main():
    while True:
        print("\n========================================")
        print(" ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE")
        print(" Last Name: COLONGON")
        print("========================================")
        print("[1] Binary Tree Traversals (BFS & DFS)")
        print("[2] Graph Traversals (BFS & DFS)")
        print("[3] Exit")

        choice = input(
            "\nEnter your choice (1, 2, or 3): "
        ).strip()  # Use .strip() to handle spaces safely

        if choice == "1":
            run_binary_tree()
        elif choice == "2":
            run_graph()
        elif choice == "3":
            print("\nExiting program. Good luck with your assessment!")
            break
        else:
            print(
                "\n[!] Invalid choice. Please enter 1, 2, or 3 to make your selection."
            )


if __name__ == "__main__":
    main()