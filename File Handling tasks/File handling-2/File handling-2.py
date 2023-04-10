def count_uppercase_chars(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        uppercase_count = 0
        for line in input_file:
            for char in line:
                if char.isupper():
                    uppercase_count += 1
        output_file.write(f"The number of uppercase characters in {input_filename} is {uppercase_count}.")
        
count_uppercase_chars("f1.txt", "output.txt")        