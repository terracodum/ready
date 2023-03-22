def number(bus_stops):
    num1 = 0
    num2 = 0
    for i in range(len(bus_stops)):
        num1 += bus_stops[i][0]
        num2 += bus_stops[i][1]
    return num1 - num2
