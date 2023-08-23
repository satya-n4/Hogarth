def sort_odd_numbers(arr):
    odd_numbers = [x for x in arr if x % 2 != 0]
    odd_numbers.sort()
    odd_index = 0

    sorted_arr = []
    for num in arr:
        if num % 2 != 0:
            sorted_arr.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            sorted_arr.append(num)
    
    return sorted_arr
