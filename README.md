# Two-Pointers
Contains my answers for LeetCode's Two Pointers group of problems


Two Pointers Explanations


    Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

My Code:

class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        # First, the non alphanumeric characters are purged and set to a lower case
        s2 = ""
        print(f"Original string: {s}")
       
        for i in s:
            if i.isalnum():
                s2 = s2 + i

        s2 = s2.lower()
        print(f"Cleaned string: {s2}")


        # now the pointers are placed on the beginning and end of cleaned string and are used to find a palindrome
        i = 0
        j = len(s2) - 1

        while i < j:

            if s2[i] == s2[j]:
                i += 1
                j -= 1

            else:
                return False
               
        return True



Explanation: To begin, we will remove all of the spaces and non-alphanumeric characters, leaving only a string with no spaces. 

With this done, we will place pointers at the beginning and end of the string. These pointers will be used to compare each character. These points will get closer to the center with each correct comparison. If pointer i is ever equal to or greater than j, we’ve finished comparing, and have found a valid palindrome.



    Two Sum II - Input Array is Sorted

two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].



	My Code:

class Solution2:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i != j:
            res = numbers[i] + numbers[j]


            if res == target:
                Arr = []
                Arr.append(i + 1)
                Arr.append(j + 1)
                return Arr


            elif res < target:
                i += 1


            elif res > target:
                j -= 1


        return []

Explanation: We set two pointers. One at the beginning, and one at the end. We calculate the sum of the values at these two indexes. If these two values match our given target value, we add the two indexes (after adding 1 to both to match the format of the correct answer), and return the array

If the sum is lower than our target value, we increment the i pointer in order to increase the sum value.

If the sum is greater than our target, we decrement the j pointer to decrease the sum value.




    3sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.



Example 3: 

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


	My Code:

class Solution:
    def threeSum(self, nums):

        results = []
        nums = sorted(nums)
        
        length_nums = len(nums)
        # This will iterate over all but the last two elements in the list.
        for i in range(length_nums - 2):
            # Places our two pointers. j is right after i, k is placed at the last element of the array.
            j = i + 1
            k = length_nums - 1
            
            while j < k:
                # A valid triplet has been found.
                if nums[i] == (-1 * (nums[j] + nums[k])):
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                # if the values of indexes j and k are GREATER than i, we nned a smaller value. We decrement k in this case  
                elif nums[i] < (-1 * (nums[j] + nums[k])):
                    k -= 1

                # the values of index j and k are LESSER than i we need a greater value. we increment j in this case.
                elif nums[i] > (-1 * (nums[j] + nums[k])):
                    j += 1

        # We've finished going through the array, now we return our results array.
        return results


Explanation: 

  Step 1: Prepare for solutions

To start, i’ll sort the array. This will make it easier to find the necessary triplets

In addition, I’ll set up an array called “results” in order to store valid triplets.
	
  Step 2: Set the indexes

Once sorted, we will place our three pointers. 

pointer “i” will be first placed on the first index of the sorted array. I will iterate through the array until the third from the end element (to leave space for the other two pointers)

Pointer “j” will be placed at the index right after i for each interaction. 

Pointer “k” will be placed at the last index for each iteration

  Step 3: Find triplets

Now we can start searching for triplets. The game plan is as follows:

nums[i] = -(nums[j] + nums[k])

I.e. the value at index i should match the negative result of the values at indexes j and k. If this is true, then the total values should equal zero.


If the values of j and k are greater than i, then we need a smaller value. This is achieved by decrementing the k index.

If the values of j and k and lesser than i, then we need a greater value. This is achieved by incrementing the j index.


If the value of j matches or exceeds k, it is time to move i for the next iteration.


  Step 4: Storing Valid Triplets

When a valid triplet is found, all three will be added to the results array. Index j is incremented, and index k are decremented, and the search continues.

When we have gone through all possible indexes, we return the results array. 


Container With the Most Water

You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose two bars to form a container. Return the maximum amount of water a container can store

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36


Example 2:

Input: height = [2,2,2]

Output: 4


My Code:


class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1

        # sets the initial max are for the array. 
        bar_height = min(height[i],height[j])
        max_area = bar_height * (len(height) - 1)

        while i < j:

            # if the bar at i is lower in height, we increment i until we find a taller bar. if j is lower in height, we decrement j.
            if height[i] < height[j]:

                curr_bar_height = height[i]
                i += 1
                # will search for a taller bar until one is found, or we hit the limit.
                while curr_bar_height > height[i] and i < j:
                    i += 1
            
            # we are finding a taller bar for j
            else:
                curr_bar_height = height[j]
                j -= 1

                while curr_bar_height > height[j] and i < j:
                    j-= 1

            
            # with i or j updated we calculate the area and compare with our current max
            bar_height = min(height[i],height[j])
            curr_area = bar_height * (j - i)

            max_area = max(max_area, curr_area)

        return max_area


Explanation:

    Step 1: Place the pointers at their initial positions

Place index i at the beginning of the list, and j at the end. Using their values and the distance between them, calculate the area of the container. This will serve as our max.

The area will be the square of the smaller of the two bars.
	
    Step 2: Find the next bar.

With our initial max found, we need to find another bar to check.  This will be done by moving the pointer of the smaller bar. 

I.e if i is the smaller bar, we increment i. If J is the smaller bar, we decrement j. The bar will move until we find a bar that is greater in height than the last used bar. 

Once a new bar is found, the area is calculated, and checked against the current max. We will keep the greater value.

Once i is no longer less than j, we return the result.


