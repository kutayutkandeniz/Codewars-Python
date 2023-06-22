import operator
#import built in operator module
def basic_op(operatoro, value1, value2):
    
#Dictionary maps values from operatoro to functions
    opmap = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv          
    }
# Convert operatoro string to  actual operator 
    operation = opmap[operatoro]
    
    results = operation(value1, value2)
    return results
