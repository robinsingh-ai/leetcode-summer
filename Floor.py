

def binary_search(arr,target):
    start = 0 
    end = len(arr)-1
    while start<=end:
        mid = start+(end-start)//2
        if target<=arr[mid]:
            end = mid-1
        elif target>arr[mid]:
            start = mid+1
        else:
            return mid
    return end

if __name__ == "__main__":
    arr =  [2,5,8,10,12,18,19,20]
    target = 13
    ans = binary_search(arr,target)
    print(arr[ans])

