from typing import Optional, Tuple

from Tree.binary_tree import TreeNode


# https://leetcode.com/problems/binary-tree-preorder-traversal
# O(N) T - O(N) S
class PreorderTraversal:
    def recursive_traverse(
        self,
        node: Optional[TreeNode],
        preorder_list: list[int],
    ) -> list[int]:
        if node:
            preorder_list.append(node.value)
            self.recursive_traverse(node.left_child, preorder_list)
            self.recursive_traverse(node.right_child, preorder_list)

        return preorder_list

    def iterative_traverse(
        self,
        root: Optional[TreeNode],
    ) -> list[int]:
        preorder_list = []
        node_stack: list[TreeNode] = [root]

        while node_stack:
            node = node_stack.pop()
            preorder_list.append(node.value)

            if node.right_child:
                node_stack.append(node.right_child)
            if node.left_child:
                node_stack.append(node.left_child)

        return preorder_list


# https://leetcode.com/problems/binary-tree-inorder-traversal
# O(N) T - O(N) S
class InorderTraversal:
    def recursive_traverse(
        self,
        node: Optional[TreeNode],
        inorder_list: list[int],
    ) -> list[int]:
        if node:
            self.recursive_traverse(node.left_child, inorder_list)
            inorder_list.append(node.value)
            self.recursive_traverse(node.right_child, inorder_list)

        return inorder_list

    def iterative_traverse(
        self,
        root: Optional[TreeNode],
    ) -> list[int]:
        inorder_list = []
        node_stack: list[Tuple(TreeNode, bool)] = [(root, False)]

        while node_stack:
            node, is_visited = node_stack.pop()
            if is_visited:
                inorder_list.append(node.value)
            else:
                if node.left_child:
                    node_stack.append((node.right_child, False))
                node_stack.append((node, True))
                if node.right_child:
                    node_stack.append((node.left_child, False))

        return inorder_list


# https://leetcode.com/problems/binary-tree-postorder-traversal
# O(N) T - O(N) S
class PostorderTraversal:
    def recursive_traverse(
        self,
        node: Optional[TreeNode],
        postorder_list: list[int],
    ) -> list[int]:
        if node:
            self.recursive_traverse(node.left_child, postorder_list)
            self.recursive_traverse(node.right_child, postorder_list)
            postorder_list.append(node.value)

        return postorder_list

    def iterative_traverse(
        self,
        root: Optional[TreeNode],
    ) -> list[int]:
        postorder_list = []
        node_stack: list[Tuple(TreeNode, bool)] = [(root, False)]

        while node_stack:
            node, is_visited = node_stack.pop()
            if is_visited:
                postorder_list.append(node.value)
            else:
                node_stack.append((node, True))
                if node.right_child:
                    node_stack.append((node.right_child, False))
                if node.left_child:
                    node_stack.append((node.left_child, False))

        return postorder_list
