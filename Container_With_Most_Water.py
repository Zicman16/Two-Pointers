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

                




                




Sol = Solution()

# height = [1,7,2,5,4,7,3,6]
# height = [2,2,2]
height = [1,2,3,4]  # Expected output: 4

res = Sol.maxArea(height)

print(f"Maximum area of water held: {res}")