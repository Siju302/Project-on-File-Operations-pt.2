# Program to eliminate repeated lines from a file

# Creating the output file
outputFile = open('updatedbooks.txt', "w")

# Reading the input file
inputFile = open('books.txt', "r")

# holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines....")
# Iterating each line in the file
for line in inputFile:

    # checking if line is unique
    if line not in lines_seen_so_far:

        # write unique lines in output file
        outputFile.write(line)

        # adds unique lines to lines_seen_so_far
        lines_seen_so_far.add(line)

# closing the file
inputFile.close()
outputFile.close()