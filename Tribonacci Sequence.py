def tribonacci(signature, n):
      
    if n == 0:
        return []
    elif n == 1:
        signature.pop(1)
        signature.pop(1)
        return signature
    elif n == 2:
        signature.pop(2)
        return signature
    else:   
        tribo = []
        tribo.append(signature[0])
        tribo.append(signature[1])
        tribo.append(signature[2])
        [tribo.append(tribo[i -1] + tribo[i -2] + tribo[i -3]) for i in range(3, n)]
        
        return tribo
