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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> tmp = {k, 0};

        kthSmallestHelper(root, tmp);

        return tmp[1];
    }

    void kthSmallestHelper(TreeNode* root, vector<int>& tmp) {
        if (root == nullptr) {
            return;
        }

        kthSmallestHelper(root->left, tmp);

        if (tmp[0] <= 0) return;

        tmp[0]--;
        if (tmp[0] == 0) {
            tmp[1] = root->val;
            return;
        }

        kthSmallestHelper(root->right, tmp);
    }
};
