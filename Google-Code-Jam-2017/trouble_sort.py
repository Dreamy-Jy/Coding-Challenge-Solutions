def trouble_sort(int_list):
    
    done = False

    while not done:
        done = True
        for i in range(len(int_list) -2):
            if int_list[i] > int_list[i +2]:
                done = False
                int_list[i], int_list[i +2] = int_list[i +2], int_list[i]
    
    return int_list


def find_sort_error(int_list):
    '''This method takes a list of integers that should be sorted. It 
    finds and returns the first index of an array that violates the 
    of sorting in accending order.'''


    for i in range(len(int_list) -1):
        if int_list[i] > int_list[i +1]:
            return i
    
    return -1


def check_trouble_sort(int_list):
    '''Check if the trouble sort returns expected values'''
    check_list = trouble_sort(int_list)

    check_flag = find_sort_error(check_list)

    if check_flag >= 0:
        return check_flag
    
    return 'OK'