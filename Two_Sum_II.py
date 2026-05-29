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






Sol = Solution2()
Sol_Arr = []
#Arr = [1,3,4,7,11]
Arr = [2,7,11,15]
T = 9


res = Sol.twoSum(Arr, T)

print(res)