#include<iostream>
using namespace std;

typedef struct Node{
    int val;
    struct Node *next;
}ListNode, *List;

List createList(int n)
{
    List head=(ListNode*)malloc(sizeof(ListNode));
    ListNode *p=head;
    for(int i=0;i<n;i++)
    {
        int a;
        cin>>a;
        ListNode *node=(ListNode*)malloc(sizeof(ListNode));
        node->val=a;
        p->next=node;
        p=p->next;
    }
    return head;
}


void printList(List head)
{
    List p=head->next;
    while(p)
    {
        cout<<p->val<<endl;
        p=p->next;
    }
}

void reverse(List &head)
{
    ListNode *p=head->next;
    ListNode *pre=NULL;
    while(p)
    {
        ListNode *pnext=p->next;
        p->next=pre;
        pre=p;
        p=pnext;       
    }
    head->next=pre;
}


ListNode *node_k(List head, int k)
{
    ListNode *p=head;
    for(int i=0;i<k;i++)
    {
        if(p->next)
            p=p->next;
        else
        {
            cout<<"no this node"<<endl;
            return 0;
        }
    }
    return p;
}

ListNode *node_ik(List head, int k)
{
    ListNode *p1=head;
    ListNode *pk=head;
    for(int i=0;i<k-1;i++)
    {
        if(pk->next)
            pk=pk->next;
        else
        {
            cout<<"no this node"<<endl;
            return 0;
        }
    }
    while(pk->next)
    {
        pk=pk->next;
        p1=p1->next;
    }
    return p1;
}

void insert(List &head, int i, int val)
{
    ListNode *t=(ListNode*)malloc(sizeof(ListNode));
    t->val=val;
    ListNode *p=head;
    for (int j=0; j<i;j++)
    {
        if(p->next)
            p=p->next;
        else
        {
            cout<<"no node "<<i<<endl;
            return;
        }
        
    }
    t->next=p->next;
    p->next=t;
    
    return;
}

void deleteNode(List &head, int i)
{
    ListNode *p=head;
    for(int j=0;j<i-1;j++)
    {
        if(p->next)
            p=p->next;
        else
        {
            cout<<"no this node"<<endl;
            return;
        }  
    }
    ListNode *pnn=p->next->next;
    free(p->next);
    p->next=pnn;
}

void deleteList(List &head)
{   ListNode *p=head;
    while(head)
    {   
        p=head->next;
        free(head);
        head=p;
    }
    
}

int main()
{
    int n=5;
    cout<<"input 5 number as a list"<<endl;
    List head=createList(n);
    cout<<"list : "<<endl;
    printList(head);

    cout<<"insert 6 after node 2:"<<endl;
    insert(head,2,6);
    printList(head);

    cout<<"delete node 2:"<<endl;
    deleteNode(head,2);
    printList(head);

    ListNode *k=node_k(head,2);
    ListNode *ik=node_ik(head,2);
    cout<<"node 2nd : "<<k->val<<endl;
    cout<<"node last 2nd : "<<ik->val<<endl;

    cout<<"reverse : "<<endl;
    reverse(head);
    printList(head);

    deleteList(head);
    return 0;
}
