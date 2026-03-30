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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) {
            return root;
        }

        if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else {
            if (root->left == nullptr) {
                TreeNode* tmpNode = root->right;
                delete root;
                return tmpNode;
            } else if (root->right == nullptr) {
                TreeNode* tmpNode = root->left;
                delete root;
                return tmpNode;
            } else {
                int minVal = findMinVal(root->right);
                root->val = minVal;
                root->right = deleteNode(root->right, minVal);
            }
        }

        return root;
    }

    int findMinVal(TreeNode* root) {
        while (root != nullptr && root->left != nullptr) {
            root = root->left;
        }

        return root->val;
    }
};