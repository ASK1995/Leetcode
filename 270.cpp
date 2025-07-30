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
    int closestValue(TreeNode* root, double target) {
        double closest = root->val, min_diff = INT_MAX, diff;

        while(root != NULL) {
            diff = abs(root->val - target);
            if(diff < min_diff) {
                min_diff = diff;
                closest = root->val;
            } else if ((diff == min_diff) && (closest > root->val)) {
                closest = root->val;
            }
            if(root->val > target) {
                root = root->left;
            } else {
                root = root->right;
            }
        }
        return closest;
    }
};