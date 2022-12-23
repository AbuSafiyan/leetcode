# Sort Array By Parity II
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, 'i' is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

def sortArrayByParityII(nums):

    even_num = []
    odd_num = []
    sorted_list = []

    for i in nums:
        if i%2==0:
            even_num.append(i)

        else:
            odd_num.append(i)

    for num in range(int(len(nums)/2)):
        sorted_list.append(even_num[num])
        sorted_list.append(odd_num[num])

    return sorted_list


a = [4,2,5,7]
print(sortArrayByParityII(a))