"""
Second exercise: Capitalize the first letter of all the words in a text

Create a program with the following functions:
    - "readTxtFile", that reads a text file and memorize all the lines in a list
    - "capitalizeWords", that capitalizes the first letter of each word in each line and save the result in a new list
    - "writeTxtFile", that write the capitalized text in a new text file
Test the program using the file "loremipsum.txt" and write the result is "loremipsum_cap.txt"

Note: Try to avoid capitalize(), other useful methods to modify strings are split(), upper(), join()
"""

def readTxtFile(filename):
    list_lines = []
    with open(filename) as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            else: 
                list_lines.append(line)
    return list_lines

text = readTxtFile("loremipsum.txt")
# print(text)

def capitalizeWords(uncapitalized_list):
    capitalized_list = []
    for line in uncapitalized_list:
        capitalized_line = ""
        list_words = line.split()
        # print(list_words)
        for word in list_words:
            # here each word is capitalized
            initial = word[0]
            initial = initial.upper()
            capitalized_word = initial + word[1:] + " "
            capitalized_line += capitalized_word
        capitalized_list.append(capitalized_line[:len(capitalized_line) - 1])
    return capitalized_list

capitalized_list = capitalizeWords(text)

def writeTxtFile(list):
    with open("loremipsum_cap.txt", "w") as f:
        for line in list:
            f.write(line + "\n")
    return f

writeTxtFile(capitalized_list)
