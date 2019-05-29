# 插入排序
def insertionsort(a, left, right):
    for i in range(left+1, right+1):
        tmp=a[i]   
        j=i-1
        while(j>=0):
            if a[j]>tmp:
                a[j+1]=a[j]
                j-=1
            else:
                break          
        a[j+1]=tmp

if __name__=="__main__":
    a=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6]
    insertionsort(a,0, len(a)-1)
    print(a)