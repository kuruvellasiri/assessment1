"""merged two dictionaries and add values if common keys """

def merge_dicts(d1, d2):
    result=d1.copy()
    for key,value in d2.items():
        if key in result:
            result[key]+=value
        else:
            result[key]=value
    return result


d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 15}

"""calling the function and print the dictionary"""
merged_dict=merge_dicts(d1,d2)
print(merged_dict)