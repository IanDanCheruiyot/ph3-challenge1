def merge_dicts(dict1, dict2):
    #make a copy of dict1 to start the merge
    merged_dict = dict1.copy()
    
    #loop each key-value pair in dict2
    for key, value in dict2.items():
        #if key exists in the merged dict, add the values
        if key in merged_dict:
            merged_dict[key] += value
        #else add the new key-value pair to the merged dict
        else:
            merged_dict[key] = value
    
    # Return the merged dict
    return merged_dict

dict1 = {'apple': 7, 'pineapple': 68, 'grape': 91}
dict2 ={'mango': 10, 'grape': -80, 'guava': 30, 'pineapple': 28}

print(merge_dicts(dict1, dict2))