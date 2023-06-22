def open_or_senior(data):
    
    output = []
    
    for a, b in data:
        
        if a >= 55 and b > 7 :
            output.append("Senior")
        else:            
            output.append("Open")
        
    
    return output
