"Бинарный поиск"

import math

def div_search(arr, min_index,max_index,search_value):
    "Бинарный поиск"
    print(min_index, max_index)
    if max_index-min_index<2:
        if arr[min_index]==search_value:
            return min_index
        if arr[max_index]==search_value:
            return max_index
        return -1

    div_index=math.floor(( min_index+max_index)/2)
    if arr[div_index]<search_value:
        return div_search(arr,div_index,max_index,search_value)
    return div_search(arr,min_index,div_index,search_value)



sortedArray=[1,3,5,6,8,23,45,67,78,90]
findIndex=div_search(sortedArray, 0,len(sortedArray)-1,8)
print (findIndex)
