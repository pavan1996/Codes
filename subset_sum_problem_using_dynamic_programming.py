def sumofSubset(arr, sum, i, dict, set):
    key = str(sum) + str(i)
    if key in dict.keys():
        return dict[key]
    
    if sum == 0:
        print(set)
        return 1
    elif sum <0:
        return 0
    elif i<0:
        return 0
        
    if(arr[i-1]>sum):
        return_item = sumofSubset(arr, sum, i-1, dict, set)
    else:
        set_with_item_included = set + [arr[i-1]]
        return_item = sumofSubset(arr, sum, i-1, dict, set) + sumofSubset(arr, sum-arr[i-1], i-1, dict,set_with_item_included)
    dict[key] = return_item
    return return_item



arr = [2, 4, 6, 10, 16, 11, 12]
i = len(arr) - 1
dict = {}
sum = 16
set = []
numberOfSubsets = sumofSubset(arr, sum, i, dict, set)
print("Number of subsets with sum = {0} is {1}".format(sum, numberOfSubsets))
