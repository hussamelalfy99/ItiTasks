def count_lines_not_starting_with_t(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            #Checking on both lowercase & uppercase
            if not line.strip().startswith(('t', 'T')):
                count += 1
    return count

count = count_lines_not_starting_with_t("file1.txt")
print(f"The number of lines in file1.txt that do not start with an alphabet 't' is {count}.")