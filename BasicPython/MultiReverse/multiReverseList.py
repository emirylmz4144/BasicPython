

def reversed_list(our_list):
    list_for_reverse=our_list[::-1]

    for value in range(len(list_for_reverse)):
        if isinstance(list_for_reverse[value],list):
           list_for_reverse[value]=reversed_list(list_for_reverse[value])

    return list_for_reverse



our_list=[1,2,[[3,4]],[[[5,6,7]]]]
to_reverse=reversed_list(our_list)

print(f"GERİ SARILMAMIŞ LİSTE {our_list}")
print(f"GERİ SARILMIŞ LİSTE   {to_reverse}")
