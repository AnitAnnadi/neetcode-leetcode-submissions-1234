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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) {
            return nullptr;
        }

        return mergeKListsHelper(lists, 0, lists.size() - 1);
    }

    ListNode* mergeKListsHelper(vector<ListNode*>& lists, int s, int e) {
        if (s > e) return nullptr;
        if (s == e) return lists[s];

        int m = (s + e) / 2;
        ListNode* leftPtr = mergeKListsHelper(lists, s, m);
        ListNode* rightPtr = mergeKListsHelper(lists, m + 1, e);

        return mergeLists(leftPtr, rightPtr);
    }

    ListNode* mergeLists(ListNode* leftPtr, ListNode* rightPtr) {
        ListNode dummy;
        ListNode* node = &dummy;

        while (leftPtr != nullptr && rightPtr != nullptr) {
            if (leftPtr->val <= rightPtr->val) {
                node->next = leftPtr;
                leftPtr = leftPtr->next;
            } else {
                node->next = rightPtr;
                rightPtr = rightPtr->next;
            }
            node = node->next;
        }

        if (leftPtr == nullptr) {
            node->next = rightPtr;
        } else {
            node->next = leftPtr;
        }

        return dummy.next;
    }
};
