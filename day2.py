def run_program(cmds):
    i = 0
    while i < len(cmds):
        num = cmds[i]
        
        if num == 1:
            first = cmds[cmds[i+1]]
            second = cmds[cmds[i+2]]
            pos = cmds[i+3]
            cmds[pos] = first + second
            i += 4
        elif num == 2:
            first = cmds[cmds[i+1]]
            second = cmds[cmds[i+2]]
            pos = cmds[i+3]
            cmds[pos] = first * second
            i += 4
        elif num == 99:
            return cmds
        else:
            i += 1

final = (run_program([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]))

#part 2

# for i in range(1,100):
#     for j in range(1,100):
#         test = run_program([1,i,j,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0])
#         if test[0] == 19690720:
#             print(100* i + j)