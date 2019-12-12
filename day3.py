# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83
a,b = open('day3_input.txt').read().split('\n')
a,b = [x.split(',') for x in [a,b]]


def get_points(data):
    xPos = 0
    yPos = 0
    length = 0
    xDict = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
    yDict = {'U': 1, 'D': -1,'R': 0, 'L': 0}

    points = {}

    for cmd in data:
        for i in range(int(cmd[1:])):
            xPos += xDict[cmd[0]]
            yPos += yDict[cmd[0]]
            length += 1
            
            if (xPos,yPos) not in points:
                points[(xPos,yPos)] = length
    
    return points


aPoints = get_points(a)
bPoints = get_points(b)

both = set(aPoints)&set(bPoints)

print(min([]))