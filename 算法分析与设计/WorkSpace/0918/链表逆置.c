#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
    int data;
    Node* next;
}Node;

void insertList(Node ** pList,int data){
    Node * newNode=(Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;

    //判断当前链表是否为空
    if(*pList==NULL){
        *pList=newNode;
    }else{
        Node * q = *pList;
        //循环找到尾节点，往尾节点后插入新结点
        while(q->next){
            q=q->next;
        }
        q->next=newNode;
    }
}
void My_print_list(Node * p1){
    Node * p =p1;
    while(p){
        printf("%d ",p->data);
        p=p->next;
    }
    printf("\n");
}

//转置
Node * reverseList1(Node * list){
    if(list == NULL){
        return NULL;
    }

    Node * pre =NULL;
    Node * next = NULL;
    Node * cur=list;

    Node * newNode = NULL;

    while(cur!=NULL){
        next = cur->next;
        if(next==NULL){
            newNode = cur;
        }
        cur->next = pre;
        pre = cur;
        cur = next;
    }

    return newNode;
}

//使用递归完成逆置
Node * reverseList2(Node * list){
    if(list->next==NULL||list==NULL){
        return list;
    }

    Node * newHead = reverseList2(list->next);
    
    list->next->next=list;
    list->next=NULL;
    return newHead;
}


int main() {
    Node * list = NULL;
    insertList(&list,100);
    insertList(&list,200);
    insertList(&list,300);
    My_print_list(list);
    reverseList1(list);
    My_print_list(list);
    return 0;
}