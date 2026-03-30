/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return node;;
        }

       unordered_map<int, Node*> nodes;

       queue<Node*> q;
       q.push(node);
       nodes[node->val] = new Node(node->val);

       while(!q.empty()) {
        int qSize = q.size();
        for(int i = 0; i < qSize; i++) {
            Node* oldNode = q.front();
            q.pop();

            for (Node* nbr : oldNode->neighbors) {
                if (!nodes.count(nbr->val)) {
                    nodes[nbr->val] = new Node(nbr->val);
                    q.push(nbr);
                }

                nodes[oldNode->val]->neighbors.push_back(nodes[nbr->val]);
            }
        }
       }

       return nodes[node->val];
    }
};


