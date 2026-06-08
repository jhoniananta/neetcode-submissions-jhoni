/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return null;
        
        int val = (root1 != null ? root1.val : 0) + (root2 != null ? root2.val : 0);
        TreeNode root = new TreeNode(val);
        Stack<TreeNode[]> stack = new Stack<>();
        stack.push(new TreeNode[] {root1, root2, root});
        
        while(!stack.isEmpty()){
            TreeNode[] nodes = stack.pop();
            TreeNode node1 = nodes[0], node2 = nodes[1], node = nodes[2];

            TreeNode left1 = node1 != null ? node1.left : null;
            TreeNode left2 = node2 != null ? node2.left : null;
            if (left1 != null || left2 != null){
                int leftVal = (left1 != null ? left1.val : 0) + (left2 != null ? left2.val : 0);
                node.left = new TreeNode(leftVal);
                stack.push(new TreeNode[]{left1, left2, node.left});
            }

            TreeNode right1 = node1 != null ? node1.right : null;
            TreeNode right2 = node2 != null ? node2.right : null;
            if (right1 != null || right2 != null) {
                int rightVal = (right1 != null ? right1.val : 0) + (right2 != null ? right2.val : 0);
                node.right = new TreeNode(rightVal);
                stack.push(new TreeNode[] {right1, right2, node.right});
            }

        }
        return root;
    }
}