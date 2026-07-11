def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    i, j = 0, 0
    new_arr = []
    
    while i < len(arr1) and j < len(arr2):      
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
        
    # Append remainings
    new_arr.extend(arr1[i:])
    new_arr.extend(arr2[j:])
    
    return new_arr
        
assert merge_sorted_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6], "Error: Failed on basic interweaving arrays"
assert merge_sorted_arrays([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6], "Error: Failed when arr2 comes completely after arr1"
assert merge_sorted_arrays([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6], "Error: Failed when arr1 comes completely after arr2"
assert merge_sorted_arrays([1, 5, 9, 10, 15], [2, 3]) == [1, 2, 3, 5, 9, 10, 15], "Error: Failed when arr1 is much longer"
assert merge_sorted_arrays([1], [2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6], "Error: Failed when arr2 is much longer"
assert merge_sorted_arrays([2, 2, 4], [1, 2, 5]) == [1, 2, 2, 2, 4, 5], "Error: Failed to handle duplicate numbers properly"
assert merge_sorted_arrays([-5, -1, 4], [-3, 0, 2]) == [-5, -3, -1, 0, 2, 4], "Error: Failed to handle negative numbers"
assert merge_sorted_arrays([], [1, 2, 3]) == [1, 2, 3], "Error: Failed when arr1 is empty"
assert merge_sorted_arrays([1, 2, 3], []) == [1, 2, 3], "Error: Failed when arr2 is empty"
assert merge_sorted_arrays([], []) == [], "Error: Failed when both arrays are empty"