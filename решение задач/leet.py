class Solution:
    def twoSum(self, nums: list[int], target: int, ok=True,result=False) -> list [int]:
       while True:
        try:
            input_str = input("Введите числа через пробел: ")
            nums = list(map(int, input_str.split()))
            target = int(input("Введите число которое желаете получить сложением двух чисел"))
        except ValueError:
            print("Введите правильный формат чисел")
            ok = False
            break
        if not ok:
            continue
        for i  in range(len(nums)):
            first = nums[i]
            for j  in range(len(nums)):
                if j !=i:
                    second = nums[j]
                    if target== second+first:
                        print([i,j])
                        result =True
                        break
                    if not result:
                        continue
                    break





Solution().twoSum([], 0)



