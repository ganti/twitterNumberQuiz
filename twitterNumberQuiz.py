

lines = ['1']
for i in range(1,10):
    counter=1
    last = ''
    ln_new = ''
    line = str(lines[-1])
    for i, l in enumerate(line):
        if last != l:
            for j in range(i,len(line)):
                try:
                    if j+1 < len(line) and line[j+1] == l:
                        counter += 1
                    else:
                        break
                finally:
                    last=l
            ln_new += str(counter)+str(l)
            counter = 1
    lines.append(ln_new)
    print(line)


#for c, l in enumerate(lines):
#    print('|   ',c, ' |     ', len(l), ' |')
