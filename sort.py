def sort_by_age(cows_list):
    return sorted(cows_list, key=lambda x: x[1])

cows = [("addie", 2), ("sal", 1), ("bella", 5), ("corona", 4)]
sorted_cows = sort_by_age(cows)
print(sorted_cows)