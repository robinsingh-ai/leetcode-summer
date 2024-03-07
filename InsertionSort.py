def sortArray(nums):
        for i in range(0,len(nums)-1):
            for j in range(i+1, 0, -1):
                if nums[j]<nums[j-1]:
                    temp = nums[j]
                    nums[j]=nums[j-1]
                    nums[j-1]=temp
                else:
                    break
        return nums

arr = [5,4,3,2,1]
ans = sortArray(arr)
print(ans)