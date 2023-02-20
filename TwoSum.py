test1 = [2,7,11,15]
target1 = 9
test2 = [3,2,4]
target2 = 6
test3 = [3,3]
target3 = 6

def twoSum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]

print("-----")
print(twoSum(test1, target1))
print("-----")
print(twoSum(test2, target2))
print("-----")
print(twoSum(test3, target3))
print("-----")