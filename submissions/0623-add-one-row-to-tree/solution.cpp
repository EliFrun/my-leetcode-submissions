/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* curr, int curr_depth, int target_depth, int val) {
        if (curr == NULL) {
            return;
        }
        if (curr_depth + 1 == target_depth) {
            curr->left = new TreeNode(val, curr->left, NULL);
            curr->right = new TreeNode(val, NULL, curr->right);
            return;
        }
        dfs(curr->left, curr_depth + 1, target_depth, val);
        dfs(curr->right, curr_depth + 1, target_depth, val);
    }

    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, NULL);
        }
        dfs(root, 1, depth, val);
        return root;
    }
};
