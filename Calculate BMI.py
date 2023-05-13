def bmi(weight, height):
    #your code here
    score = weight/(height**2)

    if score <= 18.5:
        return 'Underweight'
    elif score <= 25.0:
        return 'Normal'
    elif score <= 30.0:
        return 'Overweight'
    elif score > 30.0:
        return 'Obese'
    else: 
        return 'Inhuman'
