def sing():
    array = []
    for i in range(100):
        if i == 98:
            array.append(str(str(99 - i) + " bottle of beer on the wall," + str(99 - i) + " bottle of beer."))
            array.append(str('Take one down and pass it around, ' + "no more" + ' bottle of beer on the wall.'))
        if i == 99:
            array.append(str("No more" + " bottles of beer on the wall," + "no more" + " bottles of beer."))
            array.append(str('Go to the store and buy some more, ' + "99" + ' bottles of beer on the wall.'))
        if i == 97:
            array.append(str(str(99 - i) + " bottles of beer on the wall," + str(99 - i) + " bottles of beer."))
            array.append(str('Take one down and pass it around, ' + str(99 - i - 1) + ' bottle of beer on the wall.'))

        if i != 98 and i != 99:
            array.append(str(str(99 - i) + " bottles of beer on the wall," + str(99 - i) + " bottles of beer."))
            array.append(str('Take one down and pass it around, ' + str(99 - i - 1) + ' bottle of beer on the wall.'))
    print(array)
    return array
