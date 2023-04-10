def display_file_content(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
display_file_content("file1.txt")