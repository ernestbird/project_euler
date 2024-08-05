

def reverse_number(number: int):
    """
    Turns number into a str, 
    reverses it, and turns back into int
    """
    str_num = str(number)
    rev_str_num = str_num[::-1]
    return int(rev_str_num)


def largest_palindrome_number (n, m):
    num_list = []
    for i in range (n, 100, -1):
        for k in range(m, 100, -1):
            sum = i * k
            if sum == reverse_number(sum):
                num_list.append(sum) 
    return max(num_list)
            
print(largest_palindrome_number(999, 999))