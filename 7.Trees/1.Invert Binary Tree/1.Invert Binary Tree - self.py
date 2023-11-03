#!/usr/bin/env python3

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	def invertTree(self, root):
		if not root: return root
		
		root.left = self.invertTree(root.left)
		root.right = self.invertTree(root.right)
		
		root.left, root.right = root.right, root.left
		
		return root