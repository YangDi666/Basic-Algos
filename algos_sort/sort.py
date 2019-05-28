# 常用排序方法整理
# Di Yang

def swap(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp

# 插入排序
def insertsort(a, left, right):
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
        
# 快速排序
def median3(a, left, right):
    center=(left+right)//2
    if a[right]<a[center]:
        swap(a, right, center)
    if a[center]<a[left]:
        swap(a, center, left)
    if a[center]<a[right]:
        swap(a, center, right)
        
def partition(a, left, right):
    i=left
    j=right
    median3(a, left, right)
    pivot=a[right]

    while i<j:
        while(i<j and a[i]<=pivot):
            i+=1
        while(i<j and a[j]>=pivot):
            j-=1
        if i<j:
            swap(a, i, j)
    swap(a,i,right)
    return i

# 快速排序递归
def quicksort(a, left, right):
    
    if right-left<1:
        return
    else:
        i=partition(a, left, right)
        quicksort(a,left,i-1)
        quicksort(a, i+1,right)
        
# 快速排序非递归
def quicksort2(a, left, right):
    stack_t=[]
    stack_t.append(left)
    stack_t.append(right)
    while stack_t!=[]:
        j=stack_t.pop()
        i=stack_t.pop()
        if i<j:
            t=partition(a, i, j)
            if i<t:
                stack_t.append(i)
                stack_t.append(t-1)
            if j>t:
                stack_t.append(t+1)
                stack_t.append(j)
        
        
if __name__=="__main__":
    a=[1,8,3,6,5,5,8,7,4,6,8,56,6,8,6]
    insertsort(a,0, len(a)-1)
    print(a)
    quicksort(a,0, len(a)-1)
    print(a)
    quicksort2(a,0, len(a)-1)
    print(a)
