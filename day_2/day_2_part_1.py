

def main():
    """main logic"""
    num_safe_lines = 0
    
    with open("day_2/main.txt", 'r') as file:
        for line in file:
            line = line.strip()
            line_as_list_of_nums = line.split(" ")
            decreasing_flag = is_decreasing(line_as_list_of_nums)
            increasing_flag = is_increasing(line_as_list_of_nums)
            print(f"line {line_as_list_of_nums}, is XOR = {XOR(decreasing_flag, increasing_flag)} and {adjacent_num_diff(line_as_list_of_nums)}")
            if XOR(decreasing_flag, increasing_flag) and adjacent_num_diff(line_as_list_of_nums):
                # print(line_as_list_of_nums)
                num_safe_lines += 1
    

    print(f"The number of safe lines --> {num_safe_lines}")

def adjacent_num_diff(list_of_nums):
    """returns true is adjacent numbers differ by atleast 1 and max of 3"""
    for i in range(0, len(list_of_nums) - 1):
        if abs(int(list_of_nums[i]) - int(list_of_nums[i + 1])) not in [1, 2, 3]:
            return False
        
    return True

def XOR(a, b):
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