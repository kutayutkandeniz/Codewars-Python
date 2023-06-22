def quarter_of(month):
    
    if (month / 4) < 1:
        return 1
    elif 1 <= (month / 4) <= 1.5:
        return 2
    elif 1.5 < (month / 4) < 2.5:
        return 3
    else:
        return 4# your code here
    pass
