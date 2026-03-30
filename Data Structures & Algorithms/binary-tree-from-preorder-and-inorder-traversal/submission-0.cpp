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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTreeHelper(preorder, inorder, 0, 0, inorder.size() - 1);
    }

    TreeNode* buildTreeHelper(vector<int>& preorder, vector<int>& inorder, int preorderIndex, int start, int end) {
        if (preorderIndex >= preorder.size()) {
            return nullptr;
        }

        TreeNode* node = new TreeNode(preorder[preorderIndex]);
        
        if (start >= end) {
            return node;
        }

        int mid;
        for (int i = start; i <= end; i++) {
            if (inorder[i] == preorder[preorderIndex]) {
                mid = i;
                break;
            }
        }

        node->left = buildTreeHelper(preorder, inorder, preorderIndex + 1, start, mid - 1);
        node->right = buildTreeHelper(preorder, inorder, preorderIndex + 2, mid + 1, end);

        return node;
    }
};
