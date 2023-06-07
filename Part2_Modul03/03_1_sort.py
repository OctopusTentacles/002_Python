def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


nums = [4, 9, 7, 6, 3, 2]

selection_sort(nums)

print(nums)