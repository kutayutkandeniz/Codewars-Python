def row_sum_odd_numbers(n):
    start = n * (n-1) + 1
    sum = 0
    for i in range(n):
        
        sum = sum + start
        start = start + 2
        
    return sum
