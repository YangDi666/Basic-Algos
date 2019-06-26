#include<iostream>
using namespace std;

typedef struct Node{
    int val;
    struct Node *left;
    struct Node *right;
}TNode, *Bst;

TNode *createNode(int val)
{
    TNode *t=(TNode*)malloc(sizeof(TNode));
    t->val=val;
    return t;
}

void insertNode(Bst &t, int val){
    if(t)
    {
        if(val<t->val)
        {
            insertNode(t->left, val);
        }
        if(val>t->val)
        {
            insertNode(t->right, val);
        }
        if(val==t->val)
        {
            cout<<"value is already in the tree"<<endl;
            return;
        }
    }
    else
    {
        t=createNode(val);
    } 
}

Bst createBst(int *a, int n)
{
    Bst t;
    for(int i=0;i<n;i++)
    {
        insertNode(t, a[i]);
    }
    return t;
}

TNode *findVal(Bst bst, int val)
{
    while(bst)
    {
        if(bst->val==val)
            return bst;
        if(val<bst->val)
            bst=bst->left;
        if(val>bst->val)
            bst=bst->right;
    }
    cout<<"no this value"<<endl;
    return NULL;
}

TNode *findMin(Bst bst)
{
    if(bst)
    { 
        while(bst->left)
        {
            bst=bst->left;
        }
    }
    return bst;
}

void inorder(Bst t){
    if (!t)
        return;
    else
    {
        inorder(t->left);
        cout<<t->val<<endl;
        inorder(t->right);
    }
}

void remove(Bst &bst, int val){
    if(bst)
    {
        TNode *t=findVal(bst, val);
        TNode *m;
        if(t->left && t->right)
        {
            m=findMin(t->right);
            t->val=m->val;
            remove(t->right, m->val);
        }
        else
        {
            if(t->left)
            { 
                t->val=t->left->val;
                free(t->left);
                t->left=NULL;
            }
            if(t->right)
            { 
                t->val=t->right->val;
                free(t->right);
                t->right=NULL;
            }
            if(!t->left && !t->right)
                free(t);
        }       t=NULL; 
    
    }
    else
        return;
        
}


int main()
{ 
    int n;
    cin>>n;
    int *a=new int[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }

    Bst bst=createBst(a, n);
    inorder(bst);
    TNode *minNode=findMin(bst);
    cout<<"min:"<<maxNode->val<<endl;
    TNode *v=findVal(bst, 5);
    cout<<"5:"<<v->val<<endl;
    remove(bst, 8);
    inorder(bst);  
    return 0;
}
