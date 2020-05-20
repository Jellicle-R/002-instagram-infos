"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""
def main():
    """"
    these are the ref. that i found from internet
#    tags = "Hey guys! #stackoverflow really #rocks #rocks #announcement"
#    hash = [tag.strip("#") for tag in tags.split() if tag.startswith("#")]
#    print(hash)
    """
# open text
    txt_file = open('dolce-hash.txt', errors='ignore', encoding='utf=8')
    tags = []   # all the text
    my_sharp = []   # only # data

# put all the lines in the 'tags'
    for line in txt_file:
        tags.append(line.strip())

# here it works perfectly
#    print(tags)

# I tried to split and store the words start with #
    for line in tags:
        hash_line = []

        single_line = line.strip()
        single_line = single_line.split()
        for elem in single_line:
            if elem[0] == "#":
                hash_line.append(elem)
        hash_num = int(len(hash_line))
        hash_line.insert(0, hash_num)

        my_sharp.append(hash_line)

# and write them in csv file
    import csv

    with open("final.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(my_sharp)





    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    pass


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
