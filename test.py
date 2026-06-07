with open("DFA_script.txt") as f:
    import re
    d = {}
    line = f.readline()
    while line:
        if "section:" in line:
            line = f.readline().strip()
            if "Delta" in line:
                d[line] = []
                aux = line
                line = f.readline()
                while "END" not in line:
                    line = line.strip().split('>')
                    d[aux].append(line)
                    line = f.readline()
            else:
                d[line] = []
                aux = line
                line = f.readline().strip()
                line = re.split(r'[, ]', line)
                line = [x for x in line if x]
                d[aux] = line
                line = f.readline()
        else:
            line = f.readline()
    print(d)