def high_and_low(numbers):
    
    numbers = (numbers.split(" "))
    numbers = [int(i) for i in numbers]
    
    return str(max(numbers))+" "+str(min(numbers))
    
    # First splitting the numbers to a list , 
    # Converting the elemenst to integers with a for loop,
    # Then we print the max and min of the list as a string and concotenates
