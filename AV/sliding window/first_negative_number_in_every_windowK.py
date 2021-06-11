def first_negative_number_in_window_size_K(array, k):
    negative_number = []
    temp_store = []
    left = 0
    right = 0
    while right < len(array):
        if array[right] < 0:
            temp_store.append(array[right])
        if right - left + 1 == k:
            if not len(temp_store):
                negative_number.append(0)
            else:
                negative_number.append(temp_store[0])
                if array[left] == temp_store[0]:
                    temp_store.pop(0)
            left += 1
        right += 1
    return negative_number

print(first_negative_number_in_window_size_K([12,-1,-7,8,-15,30,16,28], 3)) #[-1, -1, -7, -15, -15, 0]