//#include <stdio.h>
//#include <stdlib.h>
//
//typedef struct Node{
//	int val;
//	struct Node* next;
//} Node;
//
//// Utilities
//void print(Node* head){
//	while( head ){
//		printf("%d ", head->val);
//		head = head->next;
//	}
//	putchar('\n');
//}
//
//Node* createNode(){
//	Node* newNode = (Node*)malloc(sizeof(Node));
//	newNode->val = 0;
//	newNode->next = NULL;
//	return newNode;
//}
//
//void push(Node** headref, int data){
//	Node* newNode = createNode();
//	newNode->next = *headref;
//	newNode->val = data;
//	*headref = newNode;
//}
//// End of utilities
//
//Node* addTwoNumbers(Node* a, Node* b){
//	Node* temp = (Node*)malloc(sizeof(Node));
//	Node* merged = temp;
//	
//	int total = 0, sum = 0, carry = 0;
//	while( a && b ){
//		Node* node = createNode();
//		node->val += carry;
//		
//		total = a->val + b->val;
//		sum = total % 10;
//		carry = total / 10;
//		
//		node->val += sum;
//		carry += node->val / 10;
//		node->val %= 10;
//		
//		temp->next = node;
//		temp = temp->next;
//		a = a->next;
//		b = b->next;
//	}
//	
//	while( a ){
//		Node* node = createNode();
//		
//		total = carry + a->val;
//		sum = total % 10;
//		carry = total / 10;
//		
//		node->val = sum;
//		
//		temp->next = node;
//		temp = temp->next;
//		a = a->next;
//	}
//	
//	while( b ){
//		Node* node = createNode();
//		
//		total = carry + b->val;
//		sum = total % 10;
//		carry = total / 10;
//		
//		node->val = sum;
//		
//		temp->next = node;
//		temp = temp->next;
//		b = b->next;
//	}
//	
//	if( carry ){
//		Node* node = createNode();
//		node->val = carry;
//		temp->next = node;
//	}
//	
//	return merged->next;
//}
//
//
//int main(int argc, char *argv[]) {
//	Node *head1 = NULL;
////	push(&head1, 3); push(&head1, 4); push(&head1, 2);
////	push(&head1, 9); push(&head1, 9); push(&head1, 9); push(&head1, 9);
////	push(&head1, 9); push(&head1, 9); push(&head1, 9);
//	push(&head1, 7); push(&head1, 3);
//	
//	Node* head2 = NULL;
////	push(&head2, 4); push(&head2, 6); push(&head2, 5);
////	push(&head2, 9); push(&head2, 9); push(&head2, 9); push(&head2, 9);
//	push(&head2, 2); push(&head2, 9);
//	
//	Node* add = addTwoNumbers(head1, head2);
//	print(add);
//	
//	return 0;
//}










#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	int val;
	struct Node* next;
} Node;

// Utilities
void print(Node* head){
	while( head ){
		printf("%d ", head->val);
		head = head->next;
	}
	putchar('\n');
}

Node* createNode(){
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->val = 0;
	newNode->next = NULL;
	return newNode;
}

void push(Node** headref, int data){
	Node* newNode = createNode();
	newNode->next = *headref;
	newNode->val = data;
	*headref = newNode;
}

int len(Node* head){
	int total = 0;
	while( head ) { head = head->next; total++; }
	return total;
}
// End of utilities

Node* addTwoNumbers(Node* a, Node* b){
	Node *head1, *head2, *add, *tail;
	if( len(a) > len(b) ) head1 = a, head2 = b, add = a, tail = a;
	else head1 = b, head2 = a, add = b, tail = b;
	
	int total = 0, sum = 0, carry = 0;
	while( head2 ){
		tail = head1;
		total = head1->val + head2->val + carry;
		sum = total % 10;
		carry = total / 10;
		
		head1->val = sum;
		carry += head1->val / 10;
		head1->val %= 10;
		
		head2 = head2->next;
		head1 = head1->next;
	}
	
	while( head1 ){
		tail = head1;
		total = carry + head1->val;
		sum = total % 10;
		carry = total / 10;
		
		head1->val = sum;
		head1 = head1->next;
	}
	
	if( carry ){
		Node* newNode = createNode();
		newNode->val = carry;
		tail->next = newNode;
	}
	
	return add;
}

int main(int argc, char *argv[]) {
	Node *head1 = NULL;
	//	push(&head1, 3); push(&head1, 4); push(&head1, 2);
	//	push(&head1, 9); push(&head1, 9); push(&head1, 9); push(&head1, 9);
	//	push(&head1, 9); push(&head1, 9); push(&head1, 9);
	push(&head1, 7); push(&head1, 3);
	
	Node* head2 = NULL;
	//	push(&head2, 4); push(&head2, 6); push(&head2, 5);
	//	push(&head2, 9); push(&head2, 9); push(&head2, 9); push(&head2, 9);
	push(&head2, 2); push(&head2, 9);
	
	Node* add = addTwoNumbers(head1, head2);
	print(add);
	
	return 0;
}
