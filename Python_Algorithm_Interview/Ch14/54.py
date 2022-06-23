from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def my_sol(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        index_dict = {}
        for i, n in enumerate(inorder):
            index_dict[n] = i

        root = TreeNode(preorder[0])
        stack = [root]

        for n in preorder[1:]:
            cur_node = TreeNode(n)
            parent = stack[-1]

            if index_dict[n] < index_dict[parent.val]:
                parent.left = cur_node
                stack.append(cur_node)

            elif index_dict[n] > index_dict[parent.val]:
                last = stack.pop()
                while stack and index_dict[n] > index_dict[stack[-1].val]:
                    last = stack.pop()

                last.right = cur_node
                stack.append(cur_node)

        return root

    def sol1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.sol1(preorder, inorder[:index])
            node.right = self.sol1(preorder, inorder[index + 1 :])

            return node
