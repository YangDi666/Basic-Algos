import insertionsort

# 快速排序
def swap(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp

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

## 递归
def quicksort(a, left, right):   
    if right-left<1:
        return
    #elif right-left<=10:
    #    insertionsort.insertionsort(a, left, right)
    else:
        i=partition(a, left, right)
        quicksort(a,left,i-1)
        quicksort(a, i+1,right)
        
## 非递归
def quicksort2(a, left, right):
    if right-left<1:
        return
    #elif right-left<=10:
    #    insertionsort.insertionsort(a, left, right)
    else:
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

### 三分区
def partition2(a, left, right):
    i=left
    j=right
    m=right-1
    median3(a, left, right)
    pivot=a[right]
    while m>=i:
        if a[m]>pivot:
            swap(a, j, m)
            j-=1
            m-=1
        elif a[m]==pivot:
            m-=1
        else:
            if m!=i:
                swap(a, m, i)
            i+=1
    return i, j

def quicksort3(a, left,  right):
    if right-left<1:
        return
    #elif right-left<=10:
    #    insertionsort.insertionsort(a, left, right)
    else:
        i, j=partition2(a, left, right)
        quicksort3(a, left, i-1)
        quicksort3(a, j+1, right)
          
        
if __name__=="__main__":
    a=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6]
    b=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6]
    c=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6]
    quicksort(a,0, len(a)-1)
    print(a)
    quicksort2(b,0, len(b)-1)
    print(b)
    quicksort3(c,0, len(c)-1)
    print(c)
