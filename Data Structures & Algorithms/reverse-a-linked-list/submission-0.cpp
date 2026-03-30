/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }

        ListNode* newHead;
        ListNode* tail = reverseListHelper(head, newHead);
        tail->next = nullptr;

        return newHead;
    }

    ListNode* reverseListHelper(ListNode* node, ListNode*& newHead) {
        if (node->next == nullptr) {
            newHead = node;
            return newHead;
        }

        ListNode* nextNode = node->next;
        ListNode* prevNode = reverseListHelper(nextNode, newHead);

        prevNode->next = node;
        return node;
    }
};
