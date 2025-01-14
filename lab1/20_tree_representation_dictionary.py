from collections import deque

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": [],
}

def bfs(tree, startNode, goalNode):
    queue = deque([(startNode, [startNode])])
    while queue:
        (node, path) = queue.popleft()
        for nextNode in tree[node]:
            if nextNode == goalNode:
                return path + [nextNode]
            else:
                queue.append((nextNode, path + [nextNode]))
    return None

startNode = "A"
goalNode = "G"
path = bfs(tree, startNode, goalNode)
print(f"Path from {startNode} to {goalNode}: {path}")
print(tree)
