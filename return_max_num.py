# return max num 

def max_number(num_list):

    # var to update max_num every iteration 
    max_num = 0

    for num in num_list:
        #update max_num if current num is greater than 
        if num > max_num:
            max_num = num

    return max_num

the_max = max_number([3, 5, 7, 9, 2, 100])

print(f'Max num ==> {the_max}')      