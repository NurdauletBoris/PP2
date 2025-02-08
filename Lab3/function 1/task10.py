def get_unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(get_unique_elements([1, 4, 1, 4, 5]))
