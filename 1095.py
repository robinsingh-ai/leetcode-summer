    """(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

    MountainArray.get(k) returns the element of the array at index k (0-indexed).
    MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

 

Constraints:

    3 <= mountain_arr.length() <= 104
    0 <= target <= 109
    0 <= mountain_arr.get(index) <= 109


    """


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        peak = self.findPeak(mountain_arr)
        print(peak)
        ans = ans = self.Binary_search(target, mountain_arr, 0, peak)
        if ans!=-1:
            return ans
        ans = self.Binary_search(target, mountain_arr, peak+1, mountain_arr.length()-1)
        return ans



    def findPeak(self, mountain_arr):
        start = 0
        end = mountain_arr.length()-1

        while start<end:
            mid  = start+(end-start)//2
            if mountain_arr.get(mid)>mountain_arr.get(mid+1):
                end=mid
            else:
                start = mid+1
        return start
        # print(start)
        # if mountain_arr.get(start)>target:
        #     ans = self.Binary_search(target, mountain_arr, 0, start)
            
        # else:
        #     ans = self.Binary_search(target, mountain_arr, start+1, mountain_arr.length()-1)
        # return ans


    def Binary_search(self, target, mountain_arr, start, end):
        isAsc = mountain_arr.get(start)<mountain_arr.get(end)

        while start<=end:
            mid = start+(end-start)//2

            if mountain_arr.get(mid)==target:
                return mid
            if isAsc:
                if target<mountain_arr.get(mid):
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target>mountain_arr.get(mid):
                    end = mid - 1
                else:
                    start = mid + 1
        
        return -1
        