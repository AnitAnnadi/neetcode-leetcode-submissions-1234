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

            for (int i = 0; i < qSize; i++) {
                TreeNode* curr = q.front();
                rightVals.push_back(curr->val);
                q.pop();

                if (curr->right) {
                    q.push(curr->right);
                } else {
                    if (curr->left) {
                        q.push(curr->left);
                    }
                }
            } 
        }

        return rightVals;
    }
};
