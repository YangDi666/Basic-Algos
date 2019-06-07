#堆排序
def swap(a, i, j):
    tem=a[i]
    a[i]=a[j]
    a[j]=tem

def shift_down(a, index, end):
    if index>end:
        print('index error!')
        return
    index_max=index
    left=2*index+1
    right=2*index+2
    if left<=end and a[index_max]<a[left]:
        index_max=left
    if right<=end and a[index_max]<a[right]:
        index_max=right
    if index_max==index:
        return
    else:
        swap(a, index, index_max)
        shift_down(a, index_max, end)

def build_heap(a): 
    end=len(a)-1
    for i in range((end-1)//2, -1, -1):
        shift_down(a, i, end)
    

def heap_sort(a):
    build_heap(a)
    end=len(a)-1
    swap(a, 0, end)
    while(end>0):
        end-=1
        shift_down(a, 0, end)   
        swap(a, 0, end)

def heapsort(a, begin, end):
    b=a[begin:end+1]
    heap_sort(b)
    a[begin:end+1]=b


if __name__=='__main__':
    a=[10,9,5,66,1,8,3,6,5,5,8,7,4,6,8,56,6,8,6]
    heapsort(a,2,8)
    print(a)
    heap_sort(a)
    print(a)
