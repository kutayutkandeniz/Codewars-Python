def are_you_playing_banjo(name):
    # Implement me!
    
    indexR = name.find("R")
    indexr = name.find("r")
    
    if indexR == 0 or indexr == 0:
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
