# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]


        def helper(node):

            if not node:
                return 0
            
            l=helper(node.left)
            r=helper(node.right)
            
            niche_hi_milgaya=l+r+node.val
            koi_ek_acha=max(l,r)+node.val
            koi_acha_nahi_he=node.val

            res[0]=max(res[0],niche_hi_milgaya,koi_ek_acha,koi_acha_nahi_he)

            return max(koi_ek_acha,koi_acha_nahi_he)

        helper(root)
        return res[0]
