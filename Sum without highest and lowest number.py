def sum_array(arr):
    if type(arr) != list:
        return 0
    elif len(arr) < 2:
        return 0 
    elif len(arr) >= 2:
        arr.sort()
        return sum(arr) - arr[0] - arr[-1]
        
    #your code here
        
