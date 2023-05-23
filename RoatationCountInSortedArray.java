/* From GFG
Given an array arr[] of size N having distinct numbers sorted in increasing order and the array has been right rotated (i.e, the last element will be cyclically shifted to the starting position of the array) k number of times, the task is to find the value of k.

Examples:  

    Input: arr[] = {15, 18, 2, 3, 6, 12}
    Output: 2
    Explanation: Initial array must be {2, 3, 6, 12, 15, 18}. 
    We get the given array after rotating the initial array twice.

    Input: arr[] = {7, 9, 11, 12, 5}
    Output: 4

    Input: arr[] = {7, 9, 11, 12, 15};
    Output: 0
 */


 class Solution {


    static int findPivot(int[] nums){
        int start = 0;
        int end = nums.length-1;
        while(start<=end){
            int mid = start+(end-start)/2;
            if(mid<end && nums[mid]>nums[mid+1]){
                return mid;
            }
            if(mid>start && nums[mid]<nums[mid-1]){
                return mid-1;
            }
            if (nums[mid]<=nums[start]){
                end = mid-1;
            }else{
                start = mid+1;
            }
        }
    return -1;
    }


    public int search(int[] nums, int target) {
        
    int pivot = findPivot(nums);
    return pivot+1;

    }

    


}