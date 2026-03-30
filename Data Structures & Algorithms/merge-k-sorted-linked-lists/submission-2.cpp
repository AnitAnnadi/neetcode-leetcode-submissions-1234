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
        if (lists.empty()) {
            return nullptr;
        }

        while (lists.size() > 1) {
            vector<ListNode*> mergedLists;

            int j = 0;
            while (j < lists.size()) {
                ListNode* l1 = lists[j];
                ListNode* l2 = (j + 1) < lists.size() ?  lists[j + 1] : nullptr;

                mergedLists.push_back(mergeLists(l1, l2));
                j += 2;
            }

            lists = mergedLists;
        }

        return lists[0];
    }

    ListNode* mergeLists(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* node = &dummy;

        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val <= l2->val) {
                node->next = l1;
                l1 = l1->next;
            } else {
                node->next = l2;
                l2 = l2->next;
            }
            node = node->next;
        }

        if (l1 == nullptr) {
            node->next = l2;
        } else if (l2 == nullptr) {
            node->next = l1;
        }

        return dummy.next;
    }
};
