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
       unordered_set<int> visited;

       Node* newNode = new Node(node->val);
       nodes[node->val] = newNode;
       cloneGraphHelper(node, newNode, nodes, visited);
       return newNode; 
    }

    void cloneGraphHelper(Node* oldNode, Node* newNode, unordered_map<int, Node*>& nodes, unordered_set<int>& visited) {
        visited.insert(oldNode->val);

        for (Node* node : oldNode->neighbors) {
            if (!nodes.count(node->val)) {
                nodes[node->val] = new Node(node->val);
            }

            newNode->neighbors.push_back(nodes[node->val]);
            if (!visited.count(node->val)) {
                cloneGraphHelper(node, nodes[node->val], nodes, visited);
            }
        }
    }
};

