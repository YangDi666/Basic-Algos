#include<iostream>
using namespace std;

typedef struct Node{
    int val;
    struct Node* left;
    struct Node* right;
}TreeNode,*Tree;

Tree createNode(int *pre, int *in, int pstart, int istart, int iend) 
{   
    if(istart>iend)
        return NULL;  
    else
    {
        TreeNode* root=(TreeNode*)malloc(sizeof(TreeNode));
        int valroot=pre[pstart];
        root->val=valroot;
        int i=istart;
        while(in[i]!=valroot && i<=iend)
        {
            i++;
        }
        root->left=createNode(pre,in,pstart+1,istart,i-1);
        root->right=createNode(pre,in,pstart+i-istart+1,i+1,iend);
        return root;
    }
       
}

Tree reconstructTree(int* pre, int* in, int len)
{
    
    return createNode(pre,in,0,0,len-1);
}
void preorder(Tree root)
{
    if (root)
    {
        cout<<root->val<<endl;
        preorder(root->left);
        preorder(root->right);
    }
}
void inorder(Tree root)
{
    if (root)
    {
        
        inorder(root->left);
        cout<<root->val<<endl;
        inorder(root->right);
    }
}

int main(){
    
    int pre[]={1,2,3,4,5,6};
    int in[]={2,3,1,5,4,6};
    int len=sizeof(in)/sizeof(int);
    Tree t=reconstructTree(pre,in,len);
    cout<<"preorder:"<<endl;
    preorder(t);
    cout<<"inorder:"<<endl;
    inorder(t);
    return 0;
}