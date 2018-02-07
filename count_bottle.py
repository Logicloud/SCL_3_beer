for i in range(45):
    a = 90 - 2 * i
    stra = str(a)
    b = a - 1
    strb = str(a - 1)
    if a < 2: 
        break
    print (stra + ' bottles of beer on the wall, take one down, pass it around, ' + strb +' bottles of beer on the wall.  ')
