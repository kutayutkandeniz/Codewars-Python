def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    if (mpg * fuel_left) >= distance_to_pump:
        return True
    elif (mpg * fuel_left) < distance_to_pump:
        return False
    else:
        return "Flying thru space"
