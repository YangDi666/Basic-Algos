#include<iostream>
using namespace std;

int fun(int* num, int S, int N)
{   int sum=0;
    for(int k=0;k<N;k++)
        sum+=num[k];
    
    if(S<-sum||S>sum)
        return 0;
    else
    {
        int **a=new int*[N];
        for(int i=0;i<N;i++)
            a[i]=new int[sum+1];

        for(int i=0;i<N;i++)
        {
            for(int j=0;j<=sum;j++)
            {
                
                if(i==0)
                {
                    a[i][j]=0;
                    if(j==num[0])
                    {
                        a[i][j]=1;
                    }
                }

                else
                {
                    if(j>sum-num[i])
                        a[i][j]=a[i-1][abs(j-num[i])];
                    else
                        a[i][j]=a[i-1][abs(j-num[i])]+a[i-1][j+num[i]];
                    
                }
                cout<<i<<j<<" "<<a[i][j]<<endl;
            }
        }
        
        return a[N-1][abs(S)];
    }
    
}
int main()
{
    int num[]={1,2,3,2};
    cout<<fun(num,8,4)<<endl;
    return 0;
}