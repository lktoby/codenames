#!/usr/bin/python3

PACKS = ["vanilla.txt", "duet.txt", "undercover.txt", "potter.txt", "cge.txt", 
         "bgg.txt", "trucker.txt", "holiday.txt", "ages.txt", "blizzard.txt", 
         "simpsons.txt", "jack.txt" ]

#
# 1. turn all words to uppercase letters
# 2. sort all words 
# 3. update the file
#
def process_file(filename):
    table = list()

    with open(filename) as f:
        for line in f:
            line = line.strip()
            table.append(line.upper())
    
    table.sort()
    with open(filename, "wt") as f:
        for word in table:
            f.write(word)
            f.write("\n")

#
# 1. removes blanks, comments, and unwanted words
# 2. turn all words to uppercase letters
# 
# Returns a list of processed words from the file 
#
def process_list(filename):
    table = list()

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if len(line) == 0 or \
               line.startswith("#") or \
               line.startswith("-") or \
               line.startswith("="):
               continue
            table.append(line.upper())
    
    return table
            
if __name__ == "__main__":
    import sys
    result = []
    
    if len(sys.argv) == 2:
        process_file(sys.argv[1])
        sys.exit(0)
    elif len(sys.argv) == 1:
        for pack in PACKS:
            words = process_list(pack)
            for word in words:
                if word in result:
                    print("warning: %s from %s already exists!"%(word, pack))
                else:
                    result.append(word)
    else:
        print("%s [FILE]"%sys.argv[0])
        sys.exit(1)
    
    #for i, w in enumerate(result):
    #    print("%d. %s"%(i+1, w))
    
    with open("codenames.txt", "wt") as f:
        for word in result:
            f.write(word)
            f.write("\n")
    