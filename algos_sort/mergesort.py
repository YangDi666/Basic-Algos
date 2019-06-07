def merge(a1, a2, left, right, end):
    i=left
    l_end=right-1
    j=right
    r_end=end
    k=left
    while i<=l_end and j<=r_end:
        if a1[i]<=a1[j]:
            a2[k]=a1[i]
            k+=1
            i+=1
        else:
            a2[k]=a1[j]
            k+=1
            j+=1
    if i<=l_end:
        while(i<=l_end):
            a2[k]=a1[i]
            k+=1
            i+=1
    else:
        while(j<=r_end):
            a2[k]=a1[j]
            k+=1
            j+=1
    a1[left:end+1]=a2[left:end+1]

# digui
def merge_sort(a1, a2, left, right):
    l=left
    r=right
    c=(left+right)//2
    if left>=right:
        return
    merge_sort(a1, a2, l, c)
    merge_sort(a1, a2, c+1, r)
    merge(a1, a2, l, c+1, r)

def mergesort(a, begin, end):
    a2=[0]*len(a)
    merge_sort(a, a2, begin, end)

# fei digui
def merge_pass(a1, a2, left, right, k):
    i=left
    while right+1-i>=2*k:    
        merge(a1, a2, i, i+k, i+2*k-1)
        i+=2*k
    if right+1-i>k:
        merge(a1,a2,i,i+k, right)
    

def mergesort2(a, begin, end):
    a2=[0]*len(a)
    k=1
    while(k<end-begin+1):
        merge_pass(a1,a2, begin, end, k)
        k*=2

if __name__=='__main__':
    a1=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6,3,15,11]
    mergesort2(a1,0,len(a1)-1)
    a2=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6,3,15,11]
    mergesort(a2,2,8)
    print(a1)
    print(a2)