
def palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False

nums = [1, 2, 3, 4, 5]
answer = []

for i_nums in range(0, len(nums)):
    if palindrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer.reverse()
        break

print('Последовательность:', nums)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)