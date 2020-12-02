import math

totalWidth = 800

stripWidth = 40

doorsAndWindows = [
    {
        'name': 'окно1',
        'left': 200,
        'right': 300,
    },
    {
        'name': 'дверь1',
        'left': 610,
        'right': 710,
    },
]

for i in range(0, math.ceil(totalWidth / stripWidth)):
    left = i * stripWidth
    right = (i + 1) * stripWidth

    for opening in doorsAndWindows:
        isLeftSideWithin = opening['left'] <= left < opening['right']
        isRightSideWithin = opening['left'] < right <= opening['right']
        if isLeftSideWithin and isRightSideWithin:
            print ('полоса #' + str(i) + ' полностью внутри ' + opening['name'])
        elif isLeftSideWithin or isRightSideWithin:
            print('полоса #' + str(i) + ' частично пересекается с ' + opening['name'])
