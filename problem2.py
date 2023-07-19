# 2sum
# Approach1: brute force 
# Time Complexity: O(n^2)
# Space Complexity: O(1)
nums = [4,9,1,0,2,3,5,6]
target = 7
result = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            result.append([nums[i],nums[j]])  #if asked for indices result.append([i,j])
print(result)



# Approach2: sort and 2 pointers 
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
nums = [4,9,1,0,2,3,5,6]
target = 7
result = []
nums.sort()
n = len(nums)
left = 0
right = n-1
while left < right:
    if nums[left] + nums[right] == target:
        result.append([nums[left],nums[right]])
    left += 1
    right -= 1

print(result)


# Approach3: Using hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)
nums = [4,9,1,0,2,3,5,6]
target = 7
result = []
hmap = {}
for i in range(len(nums)):
    n = target - nums[i]
    if n not in hmap:
        hmap[nums[i]] = i
    else:
        result.append([nums[i], nums[hmap[n]]])
print(result)



# Approach4: Using hashset
# Time Complexity: O(n)
# Space Complexity: O(n)
nums = [4,9,1,0,2,3,5,6]
target = 7
result = []
hset = set()
for i in range(len(nums)):
    if target - nums[i] in hset:
        result.append([nums[i],target-nums[i]])
    else:
        hset.add(nums[i])
print(result)


# 3 Sum
# Time Complexity: O(n^3)
# Space Complexity: O(n^3)
nums = [-1, 0, 1, 2, -1, -4]
target = 0
result = []
n = len(nums)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                triplet = [nums[i], nums[j], nums[k]]
                triplet.sort()  
                if triplet not in result:
                    result.append(triplet)
print(result)

