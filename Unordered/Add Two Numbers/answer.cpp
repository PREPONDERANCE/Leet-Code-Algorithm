#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    ListNode():val(0), next(nullptr){}
    ListNode(int data): val(data), next(nullptr){}
    ListNode(int data, ListNode* next): val(data), next(next){}
};

ListNode* addTwoNumbers(ListNode* a, ListNode* b){
    ListNode* temp = new ListNode;
    ListNode* merged = temp;
    
    int c = 0;
    while( c || a || b ){
        c += (a ? a->val:0) + (b? b->val:0);
        ListNode* newNode = new ListNode(c % 10);
        c /= 10;
        
        temp->next = newNode;
        temp = temp->next;
        
        if( a ) a = a->next;
        if( b ) b = b->next;
    }
    
    return temp->next;
}