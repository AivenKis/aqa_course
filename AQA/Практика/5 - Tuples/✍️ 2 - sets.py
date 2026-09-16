#                                                               Sets:
#                   Two lists are given: [1, 2, 3, 4] and [3, 4, 5, 6]. Find their intersection, union, and difference.

def list_operations(one_list, two_list):
    set1 = set(one_list)
    set2 = set(two_list)

    intersection_result = set1.intersection(set2)
    union_result = set1.union(set2)
    difference_result = set1.difference(set2)

    return intersection_result, union_result, difference_result

one_list = [1, 2, 3, 4]
two_list = [3, 4,  5, 6]

intersection_result, union_result, difference_result = list_operations(one_list, two_list)


print('\n' + '='*60)
print('Original lists:\n')
print(one_list, 'and', two_list)
print('\n' + '_'*60)
print('Intersection sets:', intersection_result)
print('Union sets:', union_result)
print('Difference sets:', difference_result)
print('_'*60)





