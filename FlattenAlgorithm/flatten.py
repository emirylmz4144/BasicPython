ourList = []


def flatten_function(our_list):
    for inValue in our_list:
        if isinstance(inValue, list):
            flatten_function(inValue)
        else:
            ourList.append(inValue)


flatten_function([[1, 2], [3, 4], [5, 6, 7]])
print(ourList)

