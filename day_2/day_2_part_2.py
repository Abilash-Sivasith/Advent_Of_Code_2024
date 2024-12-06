def main():
    """main logic"""
    num_safe_lines = 0
    
    with open("day_2/main.txt", 'r') as file:
        for line in file:
            line = line.strip()
            line_as_list_of_nums = line.split(" ")
            decreasing_flag = is_decreasing(line_as_list_of_nums)
            increasing_flag = is_increasing(line_as_list_of_nums)
            duplicates_flag, duplicated_number = contains_duplicate(line_as_list_of_nums)
            contains_multiple_duplicates_flag = contains_multiple_duplicates(line_as_list_of_nums)
            # print(f"line {line_as_list_of_nums}, is XOR = {XOR(decreasing_flag, increasing_flag)} and {adjacent_num_diff(line_as_list_of_nums)}")

            if XOR(decreasing_flag, increasing_flag) and not duplicates_flag:
                if (adjacent_num_diff(line_as_list_of_nums)):
                    num_safe_lines += 1
                else:
                    for i in range(0, len(line_as_list_of_nums)):
                        copy_of_list = line_as_list_of_nums[:]
                        copy_of_list.pop(i)
                        if adjacent_num_diff(copy_of_list):
                            num_safe_lines += 1
                            break
            elif duplicates_flag and not contains_multiple_duplicates_flag:
                copy = line_as_list_of_nums[:]
                copy.remove(duplicated_number)
                decreasing_flag = is_decreasing(copy)
                increasing_flag = is_increasing(copy)
                if (adjacent_num_diff(copy)) and XOR(decreasing_flag, increasing_flag):
                    num_safe_lines += 1
                    


 
    print(f"The number of safe lines --> {num_safe_lines}")

def contains_multiple_duplicates(list_of_nums):
    """returns true is there is multiple duplicates"""
    duplicate_count = 0
    seen_keys = dict()
    for num in list_of_nums:
        if num not in seen_keys:
            seen_keys[num] = 1
        else:
            duplicate_count += 1

        if duplicate_count == 2:
            return True
    
    return False


def contains_duplicate(list_of_nums):
    """returns true if the lift contains duplicates"""
    seen_keys = dict()
    for num in list_of_nums:
        if num not in seen_keys:
            seen_keys[num] = 1
        else:
            return True, num
    
    return False, -1

def adjacent_num_diff(list_of_nums):
    """returns true is adjacent numbers differ by atleast 1 and max of 3"""
    for i in range(0, len(list_of_nums) - 1):
        if abs(int(list_of_nums[i]) - int(list_of_nums[i + 1])) not in [1, 2, 3]:
            return False
        
    return True

def XOR(a, b):
    """does XOR logic between a and b"""
    if a != b:
        return True
    else:
        return False


def is_increasing(line_as_list):
    """returns true is the list is increasing"""
    prev_seen = int(line_as_list[0])
    for i in range(1, len(line_as_list)):
        if int(line_as_list[i]) < prev_seen:
            return False
        else:
            prev_seen = int(line_as_list[i])

    return True

def is_decreasing(line_as_list):
    """returns true is the list is decreasing"""
    prev_seen = int(line_as_list[0])
    for i in range(1, len(line_as_list)):
        if int(line_as_list[i]) > prev_seen:
            return False
        else:
            prev_seen = int(line_as_list[i])

    return True


main()