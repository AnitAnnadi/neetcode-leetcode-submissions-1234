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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> rightVals;
        queue<TreeNode*> q;

        if (root) {
            q.push(root);
        }

        while (q.size() > 0) {
            int qSize = q.size();
            TreeNode* curr;
            for (int i = 0; i < qSize; i++) {
                curr = q.front();
                q.pop();

                if (curr->left) {
                    q.push(curr->left);
                }

                if (curr->right) {
                    q.push(curr->right);
                }
            } 

            rightVals.push_back(curr->val);
        }

        return rightVals;
    }
};
