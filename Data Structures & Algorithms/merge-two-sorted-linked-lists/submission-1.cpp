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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode* currNode1 = list1;
        ListNode* currNode2 = list2;

        ListNode* newListNode = new ListNode(-1);
        ListNode* newListHead = newListNode;

        while(currNode1 != nullptr || currNode2 != nullptr) {

            if (currNode1 == nullptr) {
                newListNode->next = currNode2;
                break;
            } else if (currNode2 == nullptr) {
                newListNode->next = currNode1;
                break;
            } else if (currNode1->val <= currNode2->val){
                newListNode->next = currNode1;
                currNode1 = currNode1->next;
            } else {
                newListNode->next = currNode2;
                currNode2 = currNode2->next;
            }
            
            newListNode = newListNode->next;
        }

        return newListHead->next;
    }
};
