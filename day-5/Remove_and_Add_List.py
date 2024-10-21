custom_list = [10, 44, 57, 99, 11, 33, 84]
removed_element = custom_list.pop(4)
# print(removed_element)
custom_list.insert(2, removed_element)
custom_list.append(removed_element)
print(custom_list)
