def accum(s):
    return "-".join([s[i].upper() + (s[i].lower() * i) for i in range(len(s))])
    
    # s[i] accesses the character at index
    # .upper() converts it to uppercase
    # (s[i].lower() * i)  multiplies the lowercase with the index according to length   
    # these are concateneted by +
    # and this list are joined with "-"
