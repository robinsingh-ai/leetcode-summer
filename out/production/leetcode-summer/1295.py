# // Leetcode: 1295. Find Numbers with Even Number of Digits
# // Problem Statement : 
# / Given an array nums of integers, return how many of them contain an even number of digits.

 

# // Example 1:

# // Input: nums = [12,345,2,6,7896]
# // Output: 2
# // Explanation: 
# // 12 contains 2 digits (even number of digits). 
# // 345 contains 3 digits (odd number of digits). 
# // 2 contains 1 digit (odd number of digits). 
# // 6 contains 1 digit (odd number of digits). 
# // 7896 contains 4 digits (even number of digits). 
# // Therefore only 12 and 7896 contain an even number of digits.
# // Example 2:

# // Input: nums = [555,901,482,1771]
# // Output: 1 
# // Explanation: 
# // Only 1771 contains an even number of digits.
 

# // Constraints:

# // 1 <= nums.length <= 500
# // 1 <= nums[i] <= 10^5


 # nums = [12,345,2,6,7896]
        # nums_digits = [2,3,1,1,4]
        # 
        
        # 12 >> 12/10 > 2/10 > 0
        # 345 > 345/10 > 34 > 4 > 0
        # 2 > 2/10 > 0
        # 6 > 6/10 > 0

# Algo - 
# Traverse to each digit
#  - follow the above method to count the digits in a number
#  - use mudilo 2 ==0 to check individual digits counts, and Return True and Increment Count

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if self.digits(n):
                count=count+1
        return count
    
    def digits(self,num):
        digit_count = 0
        print("Counting Digits")
        while (num!=0):
            digit_count +=1
            num=num//10
            print("digit ", digit_count)

        return digit_count%2==0

        
       
        
# Solution 2
        digit_count=0
        count=0
        for n in nums:
            digit_count =0
            while(n != 0):

                n = int(n/10)
                digit_count += 1
            
            if digit_count %2 == 0:
                count += 1
        
        return count
                
                
        
                
                
        
        