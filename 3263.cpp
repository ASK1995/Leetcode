/**
 * Definition for doubly-linked list.
 * class Node {
 *     int val;
 *     Node* prev;
 *     Node* next;
 *     Node() : val(0), next(nullptr), prev(nullptr) {}
 *     Node(int x) : val(x), next(nullptr), prev(nullptr) {}
 *     Node(int x, Node *prev, Node *next) : val(x), next(next), prev(prev) {}
 * };
 */
class Solution {
public:
	vector<int> toArray(Node *head){
        Node *curr = head;
        vector<int> res;
        while(curr != NULL &&curr->prev != NULL) {
            curr = curr->prev;
        }
        while(curr != NULL && curr->next != head) {
            res.push_back(curr->val);
            curr = curr->next;
        }
        return res;
    }
};