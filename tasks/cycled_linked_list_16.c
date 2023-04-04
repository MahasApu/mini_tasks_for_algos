/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode* node1 = head;
    struct ListNode* node2 = head;

    while (node1 && node2 && node2->next){
        node1 = node1->next;
        node2 = node2->next->next;
        if(node1 == node2) break;
    }
    if (!(node2 && node2->next)) return NULL;

    node2 = head;
    while(node1 != node2){
        node1 = node1->next;
        node2 = node2->next;
    }
    return node1;
}