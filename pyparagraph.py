import os

# Open the Input File
csvpath = os.path.join('Resources','paragraph1.txt')

# Reading the CSV file in 'r' mode
f = open(csvpath,'r')
content = f.read()

print("Paragraph Analysis")
print("-------------------")

# Word count Function
def words_count(content):

    # CSV file datas are splitted using blank space
   words = content.split(" ")
   totalwords = len(words)
   return totalwords

print("Approximate Word Count: ", words_count(content))

# Line Count Function
def lines_count(content):

    # CSV file datas are splitted using '\n' newline
   lines = content.split("\n")
   totallines = len(lines)
   return totallines

print("Approximate Sentence Count: ", lines_count(content))

# Words count by Line count gives the average sentence
average_sentence = (words_count(content)/lines_count(content))
print("Average Sentence Length: ", average_sentence)

# Letters Count Function
def letters_count(content):

    # New list for storing the list of letters
    total_letters = []
    total_letters = list(content)
    
    # Looping for removing the blank spaces between the letters
    for item in total_letters:
        if item == ' ':
            total_letters.remove(item)
    
    # Total letter count looping
    count = 0
    for c in total_letters:
        count = count + 1
    return count

# Letter Count by words count gives the average letters
average_letters = (letters_count(content)/words_count(content))
print("Average Letter Count: ", average_letters)

# Closing the CSV File
f.close()
