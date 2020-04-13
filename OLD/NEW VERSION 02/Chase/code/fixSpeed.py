# Written by HAGHISH UG 2016
# ALL RIGHTS RESERVED

import math
def fixSpeed(speed, dx, dy):

    # calculate the distance
    squaredDistance = ((dy)**2) + ((dx)**2)
    distance =  math.sqrt(squaredDistance)

    # get the ratio between distance and speed
    ratio = distance/speed

    # get xHat and yHat (make sure you don't divide by 0)
    if ratio != 0:
        dxHat = math.sqrt(dx**2/ratio**2)
        dyHat = math.sqrt(dy ** 2 / ratio ** 2)
    else:
        dxHat = 0
        dyHat = 0

    # check if movement is negative or positive
    if dx < 0:
        dxHat *= -1
        
    if dy < 0:
        dyHat *= -1
    
    return (dxHat, dyHat)

