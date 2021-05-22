def count_number_of_occurances(num):
    temp_num = str(num)
    temp_dict = {}
    for num in temp_num:
        if num in temp_dict:
            temp_dict[num] += 1
        else:
            temp_dict[num] = 1
    return temp_dict

print(count_number_of_occurances(122340577073))