def main():
    """main logic"""
    num_safe_lines = 0
    
    with open("day_2/main.txt", 'r') as file:
        for line in file:
            line = line.strip()
            line_as_list_of_nums = line.split(" ")
            decreasing_flag = is_decreasing(line_as_list_of_nums)
            increasing_flag = is_increasing(line_as_list_of_nums)
            duplicate_flag, duplicated_num = contains_duplicate(line_as_list_of_nums)
            
            if XOR(decreasing_flag, increasing_flag) and adjacent_num_diff(line_as_list_of_nums) and not duplicate_flag:
                print(f"line --> {line} is SAFE")
                num_safe_lines += 1

            elif not duplicate_flag:
                for i in range(len(line_as_list_of_nums)):
                    copy = line_as_list_of_nums[:]
                    copy.pop(i)
                    increasing_flag = is_increasing(copy)
                    decreasing_flag = is_decreasing(copy)
                    if XOR(increasing_flag, decreasing_flag) and adjacent_num_diff(copy):
                        print(f"line --> {line} is SAFE")
                        num_safe_lines += 1
                        break
            

            elif duplicate_flag and not contains_multiple_duplicates(line_as_list_of_nums):
                #   print(f"line --> {line} is in")
                copy_of_list = line_as_list_of_nums[:]
                copy_of_list.remove(duplicated_num)
                increasing_flag = is_increasing(copy_of_list)
                decreasing_flag = is_decreasing(copy_of_list)
                if XOR(decreasing_flag, increasing_flag) and adjacent_num_diff(copy_of_list):
                    num_safe_lines += 1
                    print(f"line --> {line} is SAFE")

                
            
    print(f"The number of safe lines --> {num_safe_lines}")

def contains_duplicate(list_of_nums):
    """retruns true if it contains duplicates and returns the first duplicate number"""
    seen_dict = dict()
    for num in list_of_nums:
        if num not in seen_dict:
            seen_dict[num] = 1
        else:
            return (True, num)
    
    return (False, -1)

def contains_multiple_duplicates(list_of_nums):
    """returns true if the list contains multiple duplicates"""
    seen_dict = dict()
    for num in list_of_nums:
        if num not in seen_dict:
            seen_dict[num] = 1
        else:
            seen_dict[num] += 1
    
    dups_seen = 0 
    for key, value in seen_dict.items():
        if value == 2:
            dups_seen += 1
        elif value >= 3:
            return True
        
        if dups_seen >= 2:
            return True
    
    return False
    


def adjacent_num_diff(list_of_nums):
    """returns true is adjacent numbers differ by atleast 1 and max of 3"""
    for i in range(0, len(list_of_nums) - 1):
        if abs(int(list_of_nums[i]) - int(list_of_nums[i + 1])) not in [1, 2, 3]:
            return False
        
    return True

def XOR(a, b):
    """repliactes XOR logic"""
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