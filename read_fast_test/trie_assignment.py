'''
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''


# 1.递归
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        leftDepth = self.TreeDepth(pRoot.left)
        rightDepth = self.TreeDepth(pRoot.right)
        return max(leftDepth,rightDepth)+1


# 2.如果是非递归的话，可以利用广度遍历的思想，利用一个队列实现。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 非递归从层次遍历出发考虑层次遍历可以使用队列完成,每遍历一层，count+=1.
    def high(self, root):
        count = 0
        if root is None:  return count
        q = []
        q.append(root)
        while q:
            length = len(q)
            for i in range(len(q)):  # 只弹出当前层的节点，其子节点不弹出
                r = q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            count += 1
        return count
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:  return 0
        return self.high(pRoot)