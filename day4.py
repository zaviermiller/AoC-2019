#i am stupid so i will brute force it
satisfy = []
for i in range(387638,919123):
    num = str(i)

    one = False
    two = True

    for n in range(0,len(num)):
        try:
            if num[n + 1] < num[n]:
                two = False
                break
            if num[n] == num[n + 1]:
                one = True
            # if num[n] == num[n + 1] and num[n+1] == num[n+2]:
            #     one = False
        except:
            pass
    
    if one and two:
        satisfy.append(num)
    

ans = 0

for i in satisfy:
    count = {}

    for index,s in enumerate(i):
        if s in count and s == i[index - 1]:
            count[s] += 1
        else:
            count[s] = 1

    for n in count:
        if count[n] == 2:
            ans += 1
            break
    print(count)

print(ans)
