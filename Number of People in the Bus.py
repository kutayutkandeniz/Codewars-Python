def number(bus_stops):
    sum = 0
    peopleleft = 0
    for i in bus_stops:
        sum = i[0] - i[1]
        peopleleft = peopleleft + sum
    return peopleleft
