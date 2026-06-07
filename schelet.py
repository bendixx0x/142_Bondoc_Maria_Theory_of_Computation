def readFile(f):
    import re
    d = {}
    line = f.readline()
    while line:
        if "section:" in line:
            line = f.readline().strip()
            aux = line
            d[line] = []
            line = f.readline().strip()
            cnt = 0
            while "END" not in line:
                line = re.split(r'[, ]', line)
                line = [x for x in line if x]
                d[aux].append(line)
                line = f.readline().strip()
        else:
            line = f.readline()
    print(d)
    return d