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
        int count = 0;
        int minVal;

        kthSmallestHelper(root, k, count, minVal);

        return minVal;
    }

    void kthSmallestHelper(TreeNode* root, int k, int &count, int &minVal) {
        if (root == nullptr) {
            return;
        }

        kthSmallestHelper(root->left, k, count, minVal);

        if (count >= k) return;

        count += 1;
        if (count == k) {
            minVal = root->val;
            return;
        }

        kthSmallestHelper(root->right, k, count, minVal);
    }
};
