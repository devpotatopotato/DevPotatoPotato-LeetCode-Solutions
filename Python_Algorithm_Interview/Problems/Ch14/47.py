import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        queue = collections.deque([root])
        result = ["#"]
        while queue:
            cur_node = queue.popleft()
            if cur_node:
                queue.append(cur_node.left)
                queue.append(cur_node.right)

                result.append(str(cur_node.val))
            else:
                result.append("#")

        return " ".join(result)

    def deserialize(self, data):
        if data == "# #":
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2

        while queue:
            cur_node = queue.popleft()
            if nodes[index] is not "#":
                cur_node.left = TreeNode(int(nodes[index]))
                queue.append(cur_node.left)
            index += 1

            if nodes[index] is not "#":
                cur_node.right = TreeNode(int(nodes[index]))
                queue.append(cur_node.right)
            index += 1
        return root
