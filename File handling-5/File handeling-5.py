with open('file1.txt', 'r') as file:
    lines = file.readlines()

del lines[2:6]

with open('file1.txt', 'w') as file:
    for line in lines:
        file.write(line)