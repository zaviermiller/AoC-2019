from itertools import permutations

def run_program(cmds, inputs):
    i = 0
    inp_index = 0

    while i < len(cmds):
        num = str(cmds[i])
        if num[-2:] == '01' or num == '1':
            if len(num) > 2 and num[-3] == '1':
                first = cmds[i+1]
            else:
                first = cmds[cmds[i+1]]
            if len(num) > 3 and num[-4] == '1':
                second = cmds[i+2]
            else:
                second = cmds[cmds[i+2]]
            pos = cmds[i+3]
            cmds[pos] = first + second
            i += 4
        elif num[-2:] == '02' or num == '2':
            if len(num) > 2 and num[-3] == '1':
                first = cmds[i+1]
            else:
                first = cmds[cmds[i+1]]
            if len(num) > 3 and num[-4] == '1':
                second = cmds[i+2]
            else:
                second = cmds[cmds[i+2]]
            pos = cmds[i+3]
            cmds[pos] = first * second
            i += 4
        elif num[-2:] == '03' or num == '3':
            cmds[cmds[i + 1]] = inputs[inp_index]
            inp_index += 1
            i += 2
        elif num[-2:] == '04' or num == '4':
            if len(num) > 2 and num[0] == '1':
                output = (cmds[i+1])
            else:
                output = (cmds[cmds[i+1]])
            i += 2
        elif num[-2:] == '05' or num == '5':
            if len(num) > 2 and num[-3] == '1':
                first = cmds[i+1]
            else:
                first = cmds[cmds[i+1]]
            if len(num) > 3 and num[-4] == '1':
                second = cmds[i+2]
            else:
                second = cmds[cmds[i+2]]
            
            if first != 0:
                i = second
            else:
                i += 3
        elif num[-2:] == '06' or num == '6':
            if len(num) > 2 and num[-3] == '1':
                first = cmds[i+1]
            else:
                first = cmds[cmds[i+1]]
            if len(num) > 3 and num[-4] == '1':
                second = cmds[i+2]
            else:
                second = cmds[cmds[i+2]]
            if first == 0:
                i = second
            else:
                i += 3
        elif num[-2:] == '07' or num == '7':
            pos = cmds[i + 3]
            if len(num) > 2 and num[-3] == '1':
                first = cmds[i+1]
            else:
                first = cmds[cmds[i+1]]
            if len(num) > 3 and num[-4] == '1':
                second = cmds[i+2]
            else:
                second = cmds[cmds[i+2]]
            if first < second:
                cmds[pos] = 1
            else:
                cmds[pos] = 0
            i += 4
        elif num[-2:] == '08' or num == '8':
            pos = cmds[i + 3]
            if len(num) > 2 and num[-3] == '1':
                first = cmds[i+1]
            else:
                first = cmds[cmds[i+1]]
            if len(num) > 3 and num[-4] == '1':
                second = cmds[i+2]
            else:
                second = cmds[cmds[i+2]]
            if first == second:
                cmds[pos] = 1
            else:
                cmds[pos] = 0
            i += 4


        elif num[-2:] == '99':
            return output
        else:
            i += 1
    return cmds

highest = 0

for i in permutations(range(5)):
    inp = 0
    for j in i:
        inp = (run_program([3,8,1001,8,10,8,105,1,0,0,21,42,55,76,89,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,4,9,99,3,9,102,3,9,9,101,5,9,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,1001,9,5,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99],[j,inp]))
    if inp > highest:
        highest = inp

print(highest)