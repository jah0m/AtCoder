n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

tower = list(set(nums))
print(len(tower))
