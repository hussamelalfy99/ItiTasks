list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# i use list1 as a reference of index to add with list 2
joined_list = [list1[i] + list2[i] for i in range(len(list1))]
print(joined_list)