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




# -4     ==  -1 * (-1  + 2)   |      -1 * (-1 + 1)
#              -1 * (-1)      |      -1 *  (0)
#               1             |         0




Sol = Solution()

nums = [-1,0,1,2,-1,-4]

Res = Sol.threeSum(nums)

print("The results:")
print(Res)



# nums = sorted(nums)

# print(nums)









# Practice for storing the valid triplets
# numbers = ["1","2","3","4","5"]
# i = 0
# j = 1
# k = 2
# text = numbers[i] + numbers[j] + numbers[k]
# my_list = list(text)
# print(my_list)

# Practice for making sure that i goes through all but the last 2 indexes of a list.
# numbers = ["1","2","3","4","5"]
# numbers = ["1","2","3"]

# Len_List = len(numbers)

# for i in range(Len_List - 2):
#     print(numbers[i])

