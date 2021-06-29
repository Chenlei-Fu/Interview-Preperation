class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        return self.helper(node, mapping)

    def helper(self, node: 'Node', mapping) -> 'Node':
        if not node:
            return None
        if node.val in mapping.keys():
            return mapping[node.val]  # we should return the created one instead of node!
        newNode = Node(node.val, [])
        mapping[node.val] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.helper(neighbor, mapping))
        return newNode

    # if not node:
    #     return None
    # newNode = Node(node.val, [])
    # mapping = {node.val: newNode}
    # q = deque([node])
    # while q:
    #     cur = q.popleft()
    #     for neighbor in cur.neighbors:
    #         if neighbor.val in mapping.keys():  # visited
    #             mapping[cur.val].neighbors.append(mapping[neighbor.val])
    #         else:
    #             new_neighbor = Node(neighbor.val, [])
    #             mapping[neighbor.val] = new_neighbor
    #             mapping[cur.val].neighbors.append(new_neighbor)
    #             q.append(neighbor)
    # return newNode
