#include <iostream>
using namespace std;

typedef struct node{
    int val;
    struct node *next;
}ListNode, *List;

ListNode *createList(){
    int val;  
    cin>>val;
    if (val==0){
        return NULL;
    }
    else{
        ListNode* n=(ListNode*)malloc(sizeof(ListNode));
        n->val=val;
        n->next=createList();
        return n;
    }

}

void outputList(ListNode* p){
    if (p)
    {
        cout<<p->val<<endl;
        outputList(p->next);
    }
}
void deleteList(List &p){
    free(p);
}

void insert(List &p, int i, int val)
{
    ListNode *t=(ListNode*)malloc(sizeof(ListNode));
    t->val=val;
    ListNode *pp=p;
    for (int j=0; j<i;j++)
    {
        if(pp->next)
            pp=pp->next;
        else
        {
            cout<<"error"<<endl;
            return;
        }
        
    }
    ListNode *pn=pp->next;
    pp->next=t;
    t->next=pn;
    return;

}
void inverse(List p, int k)
{
    ListNode *t=p;
    for(int i=0;i<k;i++){
        if(p->next)
            p=p->next;
        else
        {
            cout<<"error"<<endl;
        }
    }
    while(p->next)
    {
        p=p->next;
        t=t->next;
    }
    cout<<t->val<<endl; 
}

int main(){
    List p=new ListNode;
    p->next=createList();
    insert(p, 2, 8);
    outputList(p);
    inverse(p, 3);
    ListNode *t=p->next;
    p=NULL;
    cout<<t<<endl;

    return 0;
}