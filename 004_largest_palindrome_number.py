
import time

start = time.time()

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
    orig_m = m
    
    for i in range (n, 0, -1):
        for k in range(m, 0, -1):
            sum = i * k
            if sum == reverse_number(sum):
                num_list.append(sum) 
            m = orig_m
    return max(num_list)

end = time.time()
            
print(largest_palindrome_number(999, 999))
print(f"Execution time is {(end-start)*1000} ms")