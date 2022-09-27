""" 
Write code to determine how many 9’s are in the list nums and 
assign that value to the variable how_many. 
Do not use a for loop to do this.
"""


nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

how_many = 0

def cal(num_lst, num):
    how_many = 0
    i = 0
    j = len(num_lst)
    while i<j:
        if num_lst[i] == num:
            how_many += 1
        i += 1
    return how_many

how_many = cal(nums, 9)
print(how_many)

print("##########")
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
how_many = 0
for item in nums:
    if item == 9:
        how_many += 1
print(how_many)

print("##########")
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
how_many = 0
i = 0
j = len(nums)
while i < j:
    if nums[i] == 9:
        how_many += 1
    i += 1
print(how_many)


print("##########")
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
how_many = 0
i = len(nums)
while i > 0:
    #print(nums[i-1])
    if nums[i-1] == 9:
        how_many += 1
    i -= 1
print(how_many)
