from random import randint

def middle_list(first_list, secont_list):
    return tuple(element for element in first_list if element in secont_list)

list1_var = [randint(1, 10) for i in range (10)]
list2_var = [randint(1, 10) for a in range (10)]

print(middle_list(first_list=list1_var, secont_list=list2_var))