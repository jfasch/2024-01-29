import sys


with open(sys.argv[1]) as f:
    for line in f:
        stripped_line = line.strip()
        if len(stripped_line) == 0:
            continue
        if stripped_line.startswith('#'):
            continue
        print(line, end='')
