#!/usr/bin/python3

table = list()

with open("codenames.txt") as f:
    for line in f:
        if line.isspace():
            table.append(line)
            continue
        line = line.upper()
        if line not in table:
            table.append(line)
    
with open("codenames.txt", "wt") as f:
    for line in table:
        f.write(line)