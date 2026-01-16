strength = [3, 4, 1]
k = 1

def findMinimumTime(strength, k):
    first_position_accessed = {}

    for item in strength:
        first_position_accessed[item] = False
    while not all(first_position_accessed.values()):
        first_element = strength[0]
        total_value_with_each_swap = []
        iter_for_total_value_with_each_swap =0
        if not first_position_accessed[first_element]:
            first_position_accessed[first_element]= True 
            k= first_element

findMinimumTime(strength, k)
