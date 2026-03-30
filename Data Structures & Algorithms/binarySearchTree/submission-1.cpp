struct TreeNode {
    int key;
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int key, int val) {
        this->key = key;
        this->val = val;
        left = nullptr;
        right = nullptr;
    }
};

class TreeMap {
private:
    TreeNode* root;

    TreeNode* insertHelper(TreeNode* root, int key, int val) {
        if (root == nullptr) {
            return new TreeNode(key, val);
        }

        if (key > root->key) {
            root->right = insertHelper(root->right, key, val);
        } else if (key < root->key) {
            root->left = insertHelper(root->left, key, val);
        } else {
            root->val = val;
        }

        return root;
    }

    TreeNode* removeHelper(TreeNode* root, int key) {
        if (root == nullptr) {
            return root;
        }

        if (key > root->key) {
            root->right = removeHelper(root->right, key);
        } else if (key > root->key) {
            root->left = removeHelper(root->left, key);
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
                TreeNode* curr = root->right;
                while(curr->left != nullptr) {
                    curr = curr->left;
                }

                root->key = curr->key;
                root->val = curr->val;
                root->right = removeHelper(root->right, root->key);
            }
        }

        return root;
    }

    void getInOrderKeysHelper(TreeNode* root, vector<int>& keys) {
        if (root == nullptr) {
            return;
        }

        getInOrderKeysHelper(root->left, keys);
        keys.push_back(root->key);
        getInOrderKeysHelper(root->right, keys);
    }

public:
    TreeMap() {
        root = nullptr;
    }

    void insert(int key, int val) {
        root = insertHelper(root, key, val);
    }

    int get(int key) {
        TreeNode* curr = root;

        while(curr != nullptr) {
            if (key > curr->key) {
                curr = curr->right;
            } else if (key < curr->key) {
                curr = curr->left;
            } else {
                return curr->val;
            }
        }

        return -1;
    }

    int getMin() {
        if (root == nullptr) {
            return -1;
        }

        TreeNode* curr = root;
        while(curr->left != nullptr) {
            curr = curr->left;
        }

        return curr->val;
    }

    int getMax() {
        if (root == nullptr) {
            return -1;
        }
        
        TreeNode* curr = root;
        while(curr->right != nullptr) {
            curr = curr->right;
        }

        return curr->val;
    }

    void remove(int key) {
        root = removeHelper(root, key);
    }

    std::vector<int> getInorderKeys() {
        vector<int> keys;
        getInOrderKeysHelper(root, keys);

        return keys;
    }
};
